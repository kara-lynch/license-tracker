import unittest
import mysql.connector
import json
from src.credentials.credentials_manager import *
from src.config.settings import Settings
from src.request.user_request import *
from src.logger import log


class LicenseDAO:
    '''
    LicenseDAO handles license-related operations in the database, including adding,
    deleting, and searching for licenses. It is designed to process user requests
    and enforce access control by validating user credentials before executing any
    database actions.

    Methods typically include:
    - add_license: Adds a new license record to the database.
    - delete_license: Removes a license record, subject to user permissions.
    - search_license: Retrieves license information based on query parameters.

    Access to these methods is restricted based on user roles. Only authorized users
    (e.g., managers or admins) are permitted to perform certain operations.

    '''
    conn = None
    cursor = None

    def __init__(self):  
        '''
        Initializes the LicenseDAO instance by establishing a connection to the MySQL database.

        This method reads database credentials from a configuration file defined in `Settings.db_config_file()`,
        and uses them to create a shared MySQL connection and cursor for executing queries.

        Attributes:
        - LicenseDAO.conn: A class-level MySQL connection object.
        - LicenseDAO.cursor: A class-level cursor object for executing SQL statements.
        - self.cursor: An instance-level reference to the shared cursor.

        Raises:
        - FileNotFoundError: If the configuration file cannot be found.
        - json.JSONDecodeError: If the configuration file is not valid JSON.
        - mysql.connector.Error: If the database connection fails.

        '''

        config_path = Settings.db_config_file()
        with open(config_path, "r") as file:
            creds = json.load(file)

        LicenseDAO.conn = mysql.connector.connect(
            host = creds["host"],
            port = creds["port"],
            user = creds["username"],
            password = creds["password"],
            database = creds["database"]
        )  
        LicenseDAO.cursor = LicenseDAO.conn.cursor()
        self.cursor = LicenseDAO.cursor

    def load_license_by_id(self, license_obj, id):
        '''
        Loads license details from the database using the provided license ID and populates the given license object.

        Parameters:
        - license_obj: An instance of a License model or data class that will be populated with license details.
        - id (int): The unique identifier of the license to retrieve.

        Behavior:
        - Executes a SQL query to fetch license data from the 'License' table where `lid` matches the given ID.
        - If a matching record is found, populates the `license_obj` with fields such as LicenseID, Name, Version,
        DateAdded, Type, and UploaderID.
        - If no record is found, raises a `ValueError`.

        Raises:
        - ValueError: If license with specific ID is not found.

        '''

        query = 'SELECT * FROM License WHERE lid = %s'
        self.cursor.execute (query, (id,))
        result = self.cursor.fetchone()

        if result:
            license_obj.LicenseID = result['id']
            license_obj.Name = result['licenseName']
            license_obj.Version = result['version']
            license_obj.DateAdded = result['dateAdded']
            license_obj.Type = result['licenseType']
            license_obj.UploaderID = result['uploaderID']
        else:
            raise ValueError(f"No license found with ID {id}")
        

    def seeLicenses(self):
        '''
        Retrieves and compiles detailed license information from the database.

        This method performs a multi-table SQL query using LEFT JOINs to gather data from the
        `License`, `Cost`, `ExpirationDate`, and `GeogRestriction` tables. It returns a dictionary
        of license records, keyed by license ID, with each record containing:

        - name: License name
        - ver: License version
        - type: License type
        - cost: License cost (float or None)
        - curr: Currency of the cost
        - period: Billing period
        - date_of_renewal: Renewal date (formatted as YYYY-MM-DD or None)
        - expiration_date: Expiration date (formatted as YYYY-MM-DD or None)
        - restrictions: Geographic restrictions
        Returns:
        - dict: A dictionary of license records with structured metadata.

        Notes:
        - If certain fields (e.g., cost, renewal date, expiration date) are missing, their values
        will be set to `None`.

        '''

        query = ''' 
            SELECT License.id, License.licenseName, License.version, License.licenseType, Cost.price, Cost.currency, Cost.period, Cost.renewalDate, ExpirationDate.endDate, GeogRestriction.restriction
            FROM License
            LEFT JOIN Cost ON License.id = Cost.licenseID
            LEFT JOIN ExpirationDate ON License.id = ExpirationDate.licenseID
            LEFT JOIN GeogRestriction ON License.id = GeogRestriction.licenseID
            '''
        self.cursor.execute(query) 
        results = self.cursor.fetchall()
       
        records = {}
        for col in results:
            records[f"{col[0]}"] = {}
            records[f"{col[0]}"]["name"] = col[1]
            records[f"{col[0]}"]["ver"] = col[2]
            records[f"{col[0]}"]["type"] = col[3]
            if col[4] is None:
                records[f"{col[0]}"]["cost"] = None
            else:
                records[f"{col[0]}"]["cost"] = float(col[4])
            records[f"{col[0]}"]["curr"] = col[5]
            records[f"{col[0]}"]["period"] = col[6]
            if col[7] is None:
                records[f"{col[0]}"]["date_of_renewal"] = None
            else:
                records[f"{col[0]}"]["date_of_renewal"] = col[7].strftime("%Y-%m-%d")
            if col[8] is None:
                records[f"{col[0]}"]["expiration_date"] = None
            else:
                records[f"{col[0]}"]["expiration_date"] = col[8].strftime("%Y-%m-%d")
            records[f"{col[0]}"]["restrictions"] = col[9]


        return records

    def AddLicense(self, user_request, user_credentials):
        '''    
        Adds a new license record to the database, along with optional metadata such as cost,
        geographic restrictions, and expiration date.

        This method first checks whether the user has authorization to add licenses using
        `user_credentials.has_license_auth()`. If authorized, it inserts the base license
        information into the `License` table and conditionally inserts related data into
        the `Cost`, `GeogRestriction`, and `ExpirationDate` tables based on the contents
        of `user_request`.

        Parameters:
        - user_request: An object containing cleaned license data and flags indicating which
        optional fields are present (e.g., cost, restrictions, expiration).
        - user_credentials: An object representing the user's identity and permissions.

        Behavior:
        - Inserts base license data (name, version, type, uploader ID) into the `License` table.
        - Conditionally inserts cost, geographic restriction, and expiration data into their
        respective tables if present in the request.
        - Commits all changes if successful; rolls back on error.

        Returns:
        - True if all inserts succeed.
        - False if the user is unauthorized or if any database error occurs.

        Raises:
        - mysql.connector.Error: For database-related issues.
        - Exception: For unexpected errors, which are logged.

        '''

        fields = user_request.get_clean_data_dict()
        try: 
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            
            # Base info about license, always insert into this table
            license_query = ''' INSERT INTO License (licenseName, version, licenseType, dateAdded, uploaderID)
            Values(%s, %s, %s, CURRENT_DATE, %s)
            '''
            self.cursor.execute(license_query,(fields["name"], fields["ver"], fields["type"], user_credentials.employee_id()))
            newest_id = self.cursor.lastrowid
            # Remaining table inserts are optional

            # Cost insert:
            if user_request.has_cost():
                cost_query = ''' INSERT INTO Cost (licenseID, price, currency, period, renewalDate)
                VALUES(%s, %s, %s, %s, %s)
                '''
                self.cursor.execute(cost_query, (newest_id, fields["cost"], fields["curr"], fields["period"], fields["date_of_renewal"]))

            # Geographic Restriction insert:
            if user_request.has_restrictions():
                geo_query = ''' INSERT INTO GeogRestriction (licenseID, restriction)
                VALUES(%s, %s)
                '''
                self.cursor.execute(geo_query, (newest_id, fields["restrictions"]))

            # Expiration insert:
            if user_request.has_expiration():
                expiration_query = ''' INSERT INTO ExpirationDate (licenseID, endDate)
                VALUES(%s, %s)
                '''
                self.cursor.execute(expiration_query, (newest_id, fields["expiration_date"]))

            # commit all inserts to the tables
            self.conn.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False


    def DeleteLicense(self, user_request, user_credentials):
        try: 
            '''      
            Deletes a license record from the database based on the license ID provided in the user request.

            This method first checks whether the user has authorization to delete licenses using
            `user_credentials.has_license_auth()`. If authorized, it retrieves the license ID from the
            request and deletes the corresponding record from the `License` table. If foreign key
            constraints with `ON DELETE CASCADE` are properly set up, related records in child tables
            will also be deleted automatically.

            Parameters:
            - user_request: An object containing the cleaned license data, including the license ID.
            - user_credentials: An object representing the user's identity and permissions.

            Behavior:
            - Validates user authorization.
            - Deletes the license record from the `License` table.
            - Commits the transaction if successful; rolls back on error.

            Returns:
            - True if the deletion is successful.
            - False if the user is unauthorized or if any error occurs during deletion.

            Raises:
            - mysql.connector.Error: For database-related issues.
            - Exception: For unexpected errors, which are logged.

            '''
            
            #Check if user has authorization to delete records
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            licenseID = user_request.get_clean_data_dict()["licenseID"]
            
            # Now delete from parent table
            self.cursor.execute('DELETE FROM License WHERE id = %s', (licenseID,))

            # Commit license deletion from all tables
            self.conn.commit()
        
            return True

        except mysql.connector.Error as err:
            print(f"Error deleting license {licenseID}: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False




    def close(self):
        '''
        Closes the database cursor and connection.

        This method should be called when database operations are complete to ensure
        that resources are properly released and connections are not left open.

        Behavior:
        - Closes the active cursor.
        - Closes the database connection.
        
        '''

        self.cursor.close()
        self.conn.close()
