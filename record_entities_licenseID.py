import unittest
import mysql.connector
import json
from src.credentials.credentials_manager import *
from src.config.settings import Settings
from src.request.user_request import *
from src.logger import log


class LicenseDAO:
    conn = None
    cursor = None

    def __init__(self):

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
        query = ''' 
            SELECT License.id, License.licenseName, License.version, License.licenseType, Cost.price, Cost.currency, Cost.period, Cost.renewalDate, ExpirationDate.endDate, GeogRestriction.restriction
            FROM License
            LEFT JOIN Cost ON License.id = Cost.licenseID
            LEFT JOIN ExpirationDate ON License.id = ExpirationDate.licenseID
            LEFT JOIN GeogRestriction ON License.id = GeogRestriction.licenseID
            '''
        self.cursor.execute(query) 
        results = self.cursor.fetchall()

        # for col in results:
        #     print(f"License ID: {col[0]}")
        #     print(f"Name: {col[1]}")
        #     print(f"Version: {col[2]}")
        #     print(f"Type: {col[3]}")
        #     print(f"Cost: {col[4]} {col[5]}")
        #     print(f"Period: {col[6]}")
        #     print(f"Renewal Date: {col[7]}")
        #     print(f"Expiration Date: {col[8]}")
        #     print(f"Geographic Restriction: {col[9]}")
        #     print(f"\n")

        records = {}
        for col in results:
            # records[f"{col[0]}"] = {
            #     "name": col[1],
            #     "ver": col[2],
            #     "type": col[3],
            #     "cost": None, 
            #     "curr": col[5],
            #     "period": col[6],
            #     "date_of_renewal": col[7].strftime("%Y-/%m-/%d"),
            #     "expiration_date": col[8],
            #     "restrictions": col[9]
            # }

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
        fields = user_request.get_clean_data_dict()
        try: 
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

            #commit all inserts to the tables
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
            Deleting license record by ID from all child tables before deleting from License table to avoid 
            foreign key constraint errors 
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
        self.cursor.close()
        self.conn.close()




    """ 
    This represents a License object 
    From the License Tracking database:
    CREATE TABLE Licenses (
    LicenseID INT PRIMARY KEY,
    Name VARCHAR(40) NULL,
    Version VARCHAR(8) NULL,
    DateAdded VARCHAR(10) NULL,
    Type VARCHAR(20) NULL,
    UploaderID INT 
    );
    """
class License(object):
    def __init__(self, lid=0, name=None, version=None, dateadded=None, type=None, uid=0):
        self.__lid = lid             # License Identification number for each individual license
        self.__name = name           # Name of License
        self.__version = version     # Version of License
        self.__dateadded = dateadded # Date the license was added to the database
        self.__type = type           # Type of License it is 
        self.__uid = uid             # Uploader ID

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        if name != None and len(name) > 40:
            raise ValueError("Name must be 40 characters or less in length")
        else:
            self.__name = name

    @property
    def Version(self):
        return self.__version

    @Version.setter
    def Version(self,version):
        if version != None and len(version) > 8:
            raise ValueError("Version must not exceed 8 characters in lenght")
        else:
            self.__version = version

    @property
    def DateAdded(self):
        return self.__dateadded

    @DateAdded.setter
    def DateAdded(self, dateadded):
        if dateadded != None and len(dateadded) != 10:
            raise ValueError("Date Added must be 10 characters in a YYYY-MM-DD format")
        else:
            self.__dateadded = dateadded

    @property
    def Type(self):
        return self.__type

    @Type.setter
    def Type(self, type):
        if type != None and len(type) > 20:
            raise ValueError("Type must not exceed 20 characters")
        else:
            self.__type = type

    @property
    def UploaderID(self):
        return self.__uid

    @UploaderID.setter
    def UploaderID(self, uid):
        if uid is None:
            raise ValueError("Uploader ID must be provided")
        elif not isinstance(uid, int):
            raise ValueError("Uploader ID must be an integer")
        elif uid < 0:
            raise ValueError("Uploader ID must be 0 or Higher")
        else:
            self.__uid = uid    

    def __license_str__(self):
        output = "License ID: L{0}, {1}, {2}, Date Added:{3}, Type: {4}, Uploader ID: U{5}".format(self.__lid, self.__name, self.__version, self.__dateadded, self.__type, self.__uid)
        return output


    """ 
    This represents a Employee License Assignments object
    From the Licenses database:
    CREATE TABLE EmployeeLicenseAssignments ( 
        LicenseID INT PRIMARY KEY,
        EmployeeID INT,
        AssignerID INT
        );
    """

class ELA(object):

    def __init__(self, lid = 0, empid = 0, assignid = 0):
        self.__lid = lid              # License Identification number for each individual license 
        self.__empid = empid          # Employee Identification number for helping track which person(s) the license is assigned too  
        self.__assignid = assignid    # Assigner Identification number for showing which person assigned the license to other person(s) and/or device(s)

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def EmployeeID(self):
        return self.__empid

    @EmployeeID.setter
    def EmployeeID(self, empid):
        if empid is None:
            raise ValueError("Employee ID must be provided")
        elif not isinstance(empid, int):
            raise ValueError("Employee ID must be an integer")
        elif empid < 0:
            raise ValueError("Employee ID must be 0 or higher")
        else:
            self.__empid = empid

    @property
    def AssignerID(self):
        return self.__assignid

    @AssignerID.setter
    def EmployeeID(self, assignid):
        if assignid is None:
            raise ValueError("Assigner ID must be provided")
        elif not isinstance(assignid, int):
            raise ValueError("Assigner ID must be an integer")
        elif assignid < 0:
            raise ValueError("Assigner ID must be 0 or higher")
        else:
            self.__assignid = assignid

    def __ela_str__(self):
        output = "License ID: L{0} Employee ID: E{1} Assigner ID: A{2}".format(self.__lid, self.__empid, self.__assignid)
        return output


    """ 
    This represents a Computer License Assignments object
    From the Licenses database:
    CREATE TABLE ComputerLicenseAssignments ( 
        LicenseID INT PRIMARY KEY,
        ComputerID INT,
        AssignerID INT
        );
    """

class CLA(object):
    def __init__(self, lid = 0, cid = 0, aid = 0):
        self.__lid = lid    # License Identification number for each individual license
        self.__cid = cid    # Computer Identification number for showing what device(s) the license is attached too
        self.__aid = aid    # Assigner Identification number for showing who assigned the license to said device(s) and person(s)

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def ComputerID(self):
        return self.__cid

    @ComputerID.setter
    def ComputerID(self, cid):
        if cid is None:
            raise ValueError("Computer ID must be provided")
        elif not isinstance(cid, int):
            raise ValueError("Computer ID must be an integer")
        elif cid < 0:
            raise ValueError("Computer ID must be 0 or Higher")
        else:
            self.__cid = cid

    @property
    def AssignerID(self):
        return self.__aid

    @AssignerID.setter
    def AssignerID(self, aid):
        if aid is None:
            raise ValueError("Assigner ID must be provided")
        elif not isinstance(aid, int):
            raise ValueError("Assigner ID must be an integer")
        elif aid < 0:
            raise ValueError("Assigner ID must be 0 or Higher")
        else:
            self.__aid = aid

    def __cla_str__(self):
        output = "License ID: L{0} Computer ID: C{1} Assigner ID: A{2}".format(self.__lid, self.__cid, self.__aid)
        return output


    """ 
    This represents a Cost object
    From the License Tracking database:
    CREATE TABLE Cost ( 
        LicenseID INT PRIMARY KEY,
        Cost FLOAT,
        Currency VARCHAR(3) NULL,
        Period VARCHAR(12) NULL,
        DateOfRenewal VARCHAR(10) NULL
        );
    """

class Cost(object):
    def __init__(self, lid = 0, cost = 0.0, curr = None, period = None, dateRen = None):
        self.__lid = lid             # License Identification number for each individual license
        self.__cost = cost           # Cost of the license
        self.__curr = curr           # Currency that the license was paid with
        self.__period = period       # How often the license needs to be paid for
        self.__dateRen = dateRen     # The official date the license will need to be renewed

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def Cost(self):
        return self.__cost

    @Cost.setter
    def Cost(self, cost):
        if cost is None:
            raise ValueError("Cost must be provided")
        elif not isinstance(cost, float):
            raise ValueError("Cost must be an integer")
        elif cost < 0.0:
            raise ValueError("Cost must be 0 or Higher")
        else:
            self.__cost = cost

    @property
    def Currency(self):
        return self.__curr

    @Currency.setter
    def Currency(self, curr):
        if curr != None and len(curr) > 3:
            raise ValueError("Currency must be 3 characters or less in length")
        else:
            self.__curr = curr
        
    @property
    def Period(self):
        return self.__period

    @Period.setter
    def Period(self, period):
        if period != None and len(period) > 12:
            raise ValueError("Period must be 12 characters or less in length")
        else:
            self.__period = period

    @property
    def DateRenewal(self):
        return self.__dateRen

    @DateRenewal.setter
    def DateRenewal(self, dateRen):
        if dateRen != None and len(dateRen) > 10:
            raise ValueError("Date of Renewal must be 10 characters or less in length")
        else:
            self.__dateRen = dateRen
    def __cost_str__(self):
        output = "License ID: L{0} Cost: {2}{1}  Period: {3} Date of Renewal: {4}".format(self.__lid, self.__cost, self.__curr, self.__period, self.__dateRen)
        return output


    """ 
    This represents a Expiration Date object
    From the License Tracking database:
    CREATE TABLE Expiration Date ( 
        LicenseID INT PRIMARY KEY,
        DateOfExpiration VARCHAR(10) NULL
        );
    """ 

class Expiration(object):
    def __init__(self, lid = 0, date = None):
        self.__lid = lid       # License Identification number for each individual license
        self.__date = date     # Date the license expires

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def Date(self):
        return self.__date

    @Date.setter
    def Date(self, date):
        if date != None and len(date) > 10:
            raise ValueError("Date of expiration must be 10 characters or less in length")
        else:
            self.__date = date

    def __exp_str__(self):
        output = "License ID: L{0}    Date: {1}".format(self.__lid, self.__date)
        return output


    """ 
    This represents a Geographic Restrictions object
    From the License Tracking database:
    CREATE TABLE Geographic Restrictions ( 
        LicenseID INT PRIMARY KEY,
        Restrictions VARCHAR(100) NULL
        );
    """

class Restrictions(object):
    def __init__(self, lid = 0, restrict = None):
        self.__lid = lid               # License Identification number for each individual license
        self.__restrict = restrict     # Geographic restriction for where this license cannot be used

    @property
    def LicenseID(self):
        return self.__lid

    @LicenseID.setter
    def LicenseID(self, lid):
        if lid is None:
            raise ValueError("License ID must be provided")
        elif not isinstance(lid, int):
            raise ValueError("License ID must be an integer")
        elif lid < 0:
            raise ValueError("License ID must be 0 or Higher")
        else:
            self.__lid = lid

    @property
    def Restrictions(self):
        return self.__restrict

    @Restrictions.setter
    def Restrictions(self, restrict):
        if restrict != None and len(restrict) > 100:
            raise ValueError("Date of expiration must be 10 characters or less in length")
        else:
            self.__restrict = restrict

    def __restrict_str__(self):
        output = "License ID: L{0}       Geographic Restrictions: {1}".format(self.__lid, self.__restrict)
        return output




