import unittest
import mysql.connector
import json
from src.credentials.credentials_manager import *
from src.config.settings import Settings
from src.request.user_request import *
from src.logger import log


class _LicenseDAO:
    '''
    LicenseDAO handles license-related operations in the database, including adding,
    deleting, and searching for licenses. It is designed to process user requests
    and enforce access control by validating user credentials before executing any
    database actions.

    '''
    conn_employee = None
    conn_manager = None
    cursor_emp = None
    cursor_man = None
    creds = None

    def __init__(self):  
        '''
        Initializes the LicenseDAO instance by establishing a connection to the MySQL database.

        This method reads database credentials from a configuration file defined in ``Settings.db_config_file()``,
        and uses them to create a shared MySQL connection and cursor for executing queries.

        :param LicenseDAO.conn: A class-level MySQL connection object.
        :param LicenseDAO.cursor: A class-level cursor object for executing SQL statements.
        :param self.cursor: An instance-level reference to the shared cursor.

        :raise FileNotFoundError: If the configuration file cannot be found.
        :raise json.JSONDecodeError: If the configuration file is not valid JSON.
        :raise mysql.connector.Error: If the database connection fails.

        '''

        config_path = Settings.db_config_file()
        with open(config_path, "r") as file:
            self.creds = json.load(file)

    def open(self):
        _LicenseDAO.conn_manager = mysql.connector.connect(
            host = self.creds["manager-level"]["host"],
            port = self.creds["manager-level"]["port"],
            user = self.creds["manager-level"]["username"],
            password = self.creds["manager-level"]["password"],
            database = self.creds["manager-level"]["database"]
        )  
        _LicenseDAO.cursor_man = _LicenseDAO.conn_manager.cursor()
        self.cursor_man = _LicenseDAO.cursor_man

        _LicenseDAO.conn_employee = mysql.connector.connect(
            host = self.creds["employee-level"]["host"],
            port = self.creds["employee-level"]["port"],
            user = self.creds["employee-level"]["username"],
            password = self.creds["employee-level"]["password"],
            database = self.creds["employee-level"]["database"]
        )  
        _LicenseDAO.cursor_emp = _LicenseDAO.conn_employee.cursor()
        self.cursor_emp = _LicenseDAO.cursor_emp

    def load_license_by_id(self, license_obj, id):
        '''
        Loads license details from the database using the provided license ID and populates the given license object.

        :param license_obj: An instance of a License model or data class that will be populated with license details.
        :param id: The unique identifier of the license to retrieve.
        :type id: int

        :raise ValueError: If a license with the given ID is not found.

        :meta private:

        '''

        self.open()

        query = 'SELECT * FROM License WHERE lid = %s'
        self.cursor_emp.execute (query, (id,))
        result = self.cursor_emp.fetchone()

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
        ``License``, ``Cost``, ``ExpirationDate``, and ``GeogRestriction`` tables. It returns a dictionary
        of license records, keyed by license ID, with each record containing:

        - ``name``: License name
        - ``ver``: License version
        - ``type``: License type
        - ``cost``: License cost (float or None)
        - ``curr``: Currency of the cost
        - ``period``: Billing period
        - ``date_of_renewal``: Renewal date (formatted as YYYY-MM-DD or None)
        - ``expiration_date``: Expiration date (formatted as YYYY-MM-DD or None)
        - ``restrictions``: Geographic restrictions

        More information on these fields can be found on the :doc:`api` page.

        Note: If certain fields (e.g., cost, renewal date, expiration date) are missing, their values will be set to ``None``.
        
        :return: A dictionary of license records with structured metadata.
        :rtype: dict

        '''

        self.open()

        query = ''' 
            SELECT License.id, License.licenseName, License.version, License.licenseType, Cost.price, Cost.currency, Cost.period, Cost.renewalDate, ExpirationDate.endDate, GeogRestriction.restriction
            FROM License
            LEFT JOIN Cost ON License.id = Cost.licenseID
            LEFT JOIN ExpirationDate ON License.id = ExpirationDate.licenseID
            LEFT JOIN GeogRestriction ON License.id = GeogRestriction.licenseID
            '''
        try:
            self.cursor_emp.execute(query) 
            results = self.cursor_emp.fetchall()
        except Exception as e:
            log.log("ERROR", f'Database issue. {e.args[0]}')
       
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

        self.close()
        return records
    
    def seeLicenseRange(self, user_request):
        '''
        Retrieves and compiles a specific range of records from the database.
        
        This method works identically to seeLicenses(), except it takes parameters for range and offset (included in 
        the user_request object). The range determines how many records to return, while the offset determines the
        starting point in the database to pull from.
        
        :return: A dictionary of license records with structured metadata.
        :rtype: dict

        '''
        self.open()
        fields = user_request.get_clean_data_dict()
        args = []
        query = ''' 
            SELECT License.id, License.licenseName, License.version, License.licenseType, Cost.price, Cost.currency, Cost.period, Cost.renewalDate, ExpirationDate.endDate, GeogRestriction.restriction
            FROM License
            LEFT JOIN Cost ON License.id = Cost.licenseID
            LEFT JOIN ExpirationDate ON License.id = ExpirationDate.licenseID
            LEFT JOIN GeogRestriction ON License.id = GeogRestriction.licenseID
            '''
        
        if "sort_field" in fields:
            query += "ORDER BY %s "
            args.append(fields["sort_field"])
            if "ascending" in fields & fields["ascending"]:
                query += "ASC"
            else:
                query += "DESC"
        
        query += '''
        LIMIT %s OFFSET %s'''
        args.append(fields["range"])
        args.append(fields["offset"])

        try:
            self.cursor_emp.execute(query, args) 
            results = self.cursor_emp.fetchall()
        except Exception as e:
            log.log("ERROR", f'Database issue. {e.args[0]}')
       
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

        self.close()
        return records

    def AddLicense(self, user_request, user_credentials):
        '''    
        Adds a new license record to the database, along with optional metadata such as cost, geographic restrictions, and expiration date.

        This method first checks whether the user has authorization to add licenses using 
        ``user_credentials.has_license_auth()``. If authorized, it inserts the base license
        information into the ``License`` table and conditionally inserts related data into
        the ``Cost``, ``GeogRestriction``, and ``ExpirationDate`` tables based on the contents
        of ``user_request``.

        :param user_request: An object containing cleaned license data and flags indicating which optional fields are present (e.g., cost, restrictions, expiration).
        :param user_credentials: An object representing the user's identity and permissions.

        :return: True if all inserts succeed, or False if the user is unauthorized or if any database error occurs.
        :rtype: bool

        :raise mysql.connector.Error: For database-related issues.
        :raise Exception: For unexpected errors, which are logged.

        '''
        self.open()
        fields = user_request.get_clean_data_dict()
        try: 
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            
            # Base info about license, always insert into this table
            license_query = ''' INSERT INTO License (licenseName, version, licenseType, dateAdded, uploaderID)
            Values(%s, %s, %s, CURRENT_DATE, %s)
            '''
            self.cursor_man.execute(license_query,(fields["name"], fields["ver"], fields["type"], user_credentials.employee_id()))
            newest_id = self.cursor_man.lastrowid
            # Remaining table inserts are optional

            # Cost insert:
            if user_request.has_cost():
                cost_query = ''' INSERT INTO Cost (licenseID, price, currency, period, renewalDate)
                VALUES(%s, %s, %s, %s, %s)
                '''
                self.cursor_man.execute(cost_query, (newest_id, fields["cost"], fields["curr"], fields["period"], fields["date_of_renewal"]))

            # Geographic Restriction insert:
            if user_request.has_restrictions():
                geo_query = ''' INSERT INTO GeogRestriction (licenseID, restriction)
                VALUES(%s, %s)
                '''
                self.cursor_man.execute(geo_query, (newest_id, fields["restrictions"]))

            # Expiration insert:
            if user_request.has_expiration():
                expiration_query = ''' INSERT INTO ExpirationDate (licenseID, endDate)
                VALUES(%s, %s)
                '''
                self.cursor_man.execute(expiration_query, (newest_id, fields["expiration_date"]))

            # commit all inserts to the tables
            self.conn_manager.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False
        finally:
            self.close()
    
    def EditLicense(self, user_request, user_credentials):
        '''    
        Updates a license record in the database. The ID must be provided as well as any fields to be updated.

        This method first checks whether the user has authorization to edit licenses using 
        ``user_credentials.has_license_auth()``. If authorized, it updates the ``License``, 
        ``Cost``, ``GeogRestriction``, and ``ExpirationDate`` tables as needed based on the contents
        of ``user_request``.

        :param user_request: An object containing cleaned license data and flags indicating which optional fields are present (e.g., cost, restrictions, expiration).
        :param user_credentials: An object representing the user's identity and permissions.

        :return: True if all inserts succeed, or False if the user is unauthorized or if any database error occurs.
        :rtype: bool

        :raise mysql.connector.Error: For database-related issues.
        :raise Exception: For unexpected errors, which are logged.

        '''
        """
        fields = user_request.get_clean_data_dict()
        try: 
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            new_field_info = []
            
            # Assemble query for main table
            license_main_query = ''' UPDATE License 
            SET '''

            if "name" in fields:
                license_main_query += "licenseName = %s "
                new_field_info.append(fields["name"])
            
            if "ver" in fields:
                license_main_query += "version = %s "
                new_field_info.append(fields["ver"])
            
            if "type" in fields:
                license_main_query += "licenseType = %s "
                new_field_info.append(fields["type"])

            license_main_query += "/nWHERE licenseID = %s"
            new_field_info.append(fields["licenseID"])
            
            self.cursor_man.execute(license_main_query, new_field_info)

            # Cost insert:
            if user_request.has_cost():
                cost_query = ''' INSERT INTO Cost (licenseID, price, currency, period, renewalDate)
                VALUES(%s, %s, %s, %s, %s)
                '''
                self.cursor_man.execute(cost_query, (fields["licenseID"], fields["cost"], fields["curr"], fields["period"], fields["date_of_renewal"]))

            # Geographic Restriction insert:
            if user_request.has_restrictions():
                geo_query = ''' INSERT INTO GeogRestriction (licenseID, restriction)
                VALUES(%s, %s)
                '''
                self.cursor_man.execute(geo_query, (fields["licenseID"], fields["restrictions"]))

            # Expiration insert:
            if user_request.has_expiration():
                expiration_query = ''' INSERT INTO ExpirationDate (licenseID, endDate)
                VALUES(%s, %s)
                '''
                self.cursor_man.execute(expiration_query, (fields["licenseID"], fields["expiration_date"]))

            # commit all inserts to the tables
            self.conn_manager.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False
        """
        pass
    

    def DeleteLicense(self, user_request, user_credentials):
        '''      
        Deletes a license record from the database based on the license ID provided in the user request.

        This method first checks whether the user has authorization to delete licenses using
        ``user_credentials.has_license_auth()``. If authorized, it retrieves the license ID from the
        request and deletes the corresponding record from the ``License`` table. If foreign key
        constraints with ``ON DELETE CASCADE`` are properly set up, related records in child tables
        will also be deleted automatically.

        :param user_request: An object containing the cleaned license data, including the license ID.
        :param user_credentials: An object representing the user's identity and permissions.

        :return: True if the deletion is successful, or False if the user is unauthorized or if any error occurs during deletion.

        :raise mysql.connector.Error: For database-related issues.
        :raise Exception: For unexpected errors, which are logged.

        '''
        self.open()
        try: 
            
            
            #Check if user has authorization to delete records
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            licenseID = user_request.get_clean_data_dict()["licenseID"]
            
            # Now delete from parent table
            self.cursor_man.execute('DELETE FROM License WHERE id = %s', (licenseID,))

            # Commit license deletion from all tables
            self.conn_manager.commit()
        
            return True

        except mysql.connector.Error as err:
            print(f"Error deleting license {licenseID}: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False
        finally:
            self.close()
        
    def employeeAssign(self, user_request, user_credentials):
        '''    
        Adds a new employee assignment record to the database. This creates a relation between an 
        employee record and a license record.

        This method first checks whether the user has authorization to add licenses using 
        ``user_credentials.has_license_auth()``. If authorized, it inserts the assignment
        information into the ``EmployeeAssign`` table.

        :param user_request: An object containing cleaned assignment data indicating the employee
        and license to be assigned to each other.
        :param user_credentials: An object representing the user's identity and permissions.

        :return: True if the insert succeeds, or False if the user is unauthorized or if any database error occurs.
        :rtype: bool

        :raise mysql.connector.Error: For database-related issues.
        :raise Exception: For unexpected errors, which are logged.

        '''
        self.open()

        fields = user_request.get_clean_data_dict()
        try: 
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
                        
            # Prep query to insert an assignment record
            license_query = ''' INSERT INTO EmployeeAssign (licenseID, employeeID, assignerID)
            Values(%s, %s, %s)
            '''
            self.cursor_man.execute(license_query,(fields["licenseId"], fields["employeeId"], user_credentials.employee_id()))
            
            # commit insert
            self.conn_manager.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False
        finally:
            self.close()

    def employeeUnassign(self, user_request, user_credentials):
        '''      
        Deletes an employee assignment record from the database based on the license ID provided in the user request.

        This method first checks whether the user has authorization to delete licenses using
        ``user_credentials.has_license_auth()``. If authorized, it retrieves the license and employee 
        IDs from the request and deletes the corresponding record from the ``EmployeeAssign`` table.

        :param user_request: An object containing the cleaned license data, including the license ID.
        :param user_credentials: An object representing the user's identity and permissions.

        :return: True if the deletion is successful, or False if the user is unauthorized or if any error occurs during deletion.

        :raise mysql.connector.Error: For database-related issues.
        :raise Exception: For unexpected errors, which are logged.

        '''
        self.open()
        try: 
            
            
            # Check if user has authorization to delete records
            if not user_credentials.has_license_auth():
                log.log("ERROR", "User not authorized to make this request.")
                return False
            
            fields = user_request.get_clean_data_dict()
            
            # Run deletion query
            self.cursor_man.execute('DELETE FROM EmployeeAssign WHERE (licenseID = %s AND employeeID = %s)', 
                (fields["licenseId"], fields["employeeId"]))

            # Commit assignment deletion
            self.conn_manager.commit()
        
            return True

        except mysql.connector.Error as err:
            print(f"Error deleting license {fields["licenseId"]}: {err}")
            self.conn.rollback()
            return False
        except Exception as e:
            log.log("ERROR", f'Error in DB: {e.args[0]}')
            return False
        finally:
            self.close()
        
    def SeeAssignment(self, user_request, user_credentials):
        '''
        Retrieves and compiles a specific range of records from the EmployeeAssign table.
        
        This method works identically to seeLicenseRange(), except it only returns records that have been
        assigned to a specific employee. If the user is a manager, they can provide a specific employee ID
        to see all licenses assigned to that employee; if not provided, or if the user is not a manager, 
        only the licenses assigned to the current user will be returned.
        
        :return: A dictionary of license records with structured metadata.
        :rtype: dict

        '''
        self.open()
        fields = user_request.get_clean_data_dict()
        args = []

        if user_credentials.has_license_auth() & "employeeId" in fields:
            id_to_query = fields["employeeId"]
        else:
            id_to_query = user_credentials.employee_id()
        query = ''' 
            SELECT License.id, License.licenseName, License.version, License.licenseType, Cost.price, Cost.currency, Cost.period, Cost.renewalDate, ExpirationDate.endDate, GeogRestriction.restriction
            FROM License
            LEFT JOIN Cost ON License.id = Cost.licenseID
            LEFT JOIN ExpirationDate ON License.id = ExpirationDate.licenseID
            LEFT JOIN GeogRestriction ON License.id = GeogRestriction.licenseID
            LEFT JOIN EmployeeAssign ON License.id = EmployeeAssign.licenseID
            WHERE EmployeeAssign.employeeID = %s
            '''
        args.append(str(id_to_query))
        
        if "sort_field" in fields:
            query += "ORDER BY %s "
            args.append(fields["sort_field"])
            if "ascending" in fields & fields["ascending"]:
                query += "ASC"
            else:
                query += "DESC"
        
        query += '''
        LIMIT %s OFFSET %s'''
        args.append(fields["range"])
        args.append(fields["offset"])

        try:
            self.cursor_emp.execute(query, args) 
            results = self.cursor_emp.fetchall()
        except Exception as e:
            log.log("ERROR", f'Database issue. {e.args[0]}')
       
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


        self.close()
        return records


    def close(self):
        '''
        Closes the database cursor and connection.

        This method should be called when database operations are complete to ensure
        that resources are properly released and connections are not left open.
        
        '''

        self.cursor_emp.close()
        self.cursor_man.close()
        self.conn_employee.close()
        self.conn_manager.close()
