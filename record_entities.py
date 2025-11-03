""" 
 This represents a Employee object 
 From the License Tracking database:
 CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    First Name VARCHAR(50) NULL,
    Last Name VARCHAR(50) NULL,
    Title VARCHAR(30) NULL,
    Department VARCHAR(20) NULL,
    Email INT,
    Country VARCHAR(50) NULL,
    City VARCHAR(50) NULL,
    Location INT 
    );
"""

class Employees(object):
    def __init__(self, empid = 0, fn = None, ln = None, title = None, dept = 0, email = None, country = None, city = None, loc = 0):
        self.__empid = empid      # Employee ID number that is unique to each individual employee
        self.__fn = fn            # First name of employee
        self.__ln = ln            # Last name of employee
        self.__title = title      # Job title of employee
        self.__dept = dept        # Company department the employee works in
        self.__email = email      # Email of employee
        self.__country = country  # Country the employee is working from
        self.__city = city        # City employee is working from
        self.__loc = loc          # Location ID of where employee is working from
     
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
            raise ValueError("Employee ID must be 0 or Higher")
        else:
            self.__empid = empid
    
    @property
    def FirstName(self):
        return self.__fn
    
    @FirstName.setter
    def FirstName(self, fn):
        if fn != None and len(fn) > 50:
            raise ValueError("First name must be 50 characters or less in length")
        else:
            self.__fn = fn
    
    @property
    def LastName(self):
        return self.__ln
    
    @LastName.setter
    def  LastName(self, ln):
        if ln != None and len(ln) > 50:
            raise ValueError("Last name must be 50 characters or less in length")
        else:
            self.__ln = ln
    
    @property
    def Title(self):
        return self.__title
    
    @Title.setter
    def Title(self, title):
        if title != None and len(title) > 11:
            raise ValueError("Title must be 11 characters or less in length")
        else:
            self.__title = title
    
    @property
    def Department(self):
        return self.__dept
    
    @Department.setter
    def Department(self, dept):
        if dept is None:
            raise ValueError("Department ID must be provided")
        elif not isinstance(dept, int):
            raise ValueError("Department ID must be an integer")
        elif dept < 0:
            raise ValueError("Department ID value must be 0 or more")
        else:
             self.__dept = dept
    
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        if email != None and len(email) > 50:
            raise ValueError("Email must be 50 characters or less in length")
        else:
            self.__email = email
    
    @property
    def Country(self):
        return self.__country
    
    @Country.setter
    def Country(self, country):
        if country != None and len(country) > 50:
            raise ValueError("Country must be 50 characters or less in length")
        else:
            self.__country = country

    @property
    def City(self):
        return self.__city
    
    @City.setter
    def City(self, city):
        if city != None and len(city) > 50:
            raise ValueError("City must be 50 characters or less in length")
        else:
            self.__city = city
    
    @property
    def Location(self):
        return self.__loc 
    
    @Location.setter
    def Location(self, loc):
        if loc is None:
            raise ValueError("Location ID must be entered")
        elif not isinstance(loc, int):
            raise ValueError("Location ID must be an integer")
        elif loc < 0:
            raise ValueError("Location ID value must be 0 or more")
        else:
             self.__loc = loc 

    def __emp_str__(self):
        output = "Employee ID: E{0} {1} {2}, {3}  Email: {5} , Department: D{4}, Location: O{7}, {6} {8}".format(self.__empid, self.__fn, self.__ln, self.__title, self.__dept, self.__email, self.__country, self.__city, self.__loc)
        return output


""" 
 This represents a Location object 
 From the License Tracking database:
 CREATE TABLE Location (
    OfficeID INT PRIMARY KEY,
    Phone VARCHAR(50) NULL,
    Street VARCHAR(250) NULL,
    Country VARCHAR(50) NULL,
    City VARCHAR(50) NULL, 
    );
"""

class Location(object):

    def __init__(self, offid = 0, phone = None, street = None, country = None, city = None):
        self.__offid = offid         # Office ID of the specific work building
        self.__phone = phone         # Phone number to reach the office 
        self.__street = street       # Street the building is located
        self.__country = country     # Country the office building resides in
        self.__city = city           # City the office building resides in
    
    @property
    def OfficeID(self):
        return self.__offid
    
    @OfficeID.setter
    def OfficeID(self, offid):
        if offid is None:
            raise ValueError("Office ID must be entered")
        elif not isinstance(offid, int):
            raise ValueError("Office ID must be an integer")
        elif offid < 0:
            raise ValueError("Office ID value must be 0 or more")
        else:
             self.__offid = offid

    @property
    def Phone(self):
        return self.__phone
    
    @Phone.setter
    def Phone(self, phone):
        if phone != None and len(phone) > 50:
            raise ValueError("Phone must be 50 characters or less")
        else:
            self.__phone = phone
    
    @property
    def Street(self):
        return self.__street
    
    @Street.setter
    def Street(self, street):
        if street != None and len(street) > 50:
            raise ValueError("Street must be 50 characters or less in length")
        else:
            self.__street = street
    
    @property
    def Country(self):
        return self.__country
    
    @Country.setter
    def Country(self, country):
        if country != None and len(country) > 50:
            raise ValueError("Country must be 50 characters or less in length")
        else:
            self.__country = country
    
    @property
    def City(self):
        return self.__city
    
    def City(self, city):
        if city != None and len(city) > 50:
            raise ValueError("City must be 50 characters or less in length")
        else:
            self.__city = city
    
    def __loc_str__(self):
        output = "Office ID: O{0}  {2}, {4}, {3}  Phone Number: {1}".format(self.__offid, self.__phone, self.__street, self.__country, self.__city)
        return output