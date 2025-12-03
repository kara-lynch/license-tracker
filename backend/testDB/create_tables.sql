/*
	The following query performs an action of removing any of the following
    tables within the database if they exist
*/


drop table if exists Departments, Computer, Employee, 
License, Locations, Cost, EmployeeAssign, ExpirationDate, 
GeogRestriction, CompAssign;

/*
	The following query creates a table Department.
    It has ID and name as columns
*/

create table Departments (
	ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50)
);


/*
	The following query creates a table Locations.
    The columns contain information about the office
*/

create table Locations (
	id INT AUTO_INCREMENT Primary Key,
	phone VARCHAR(50),
	street VARCHAR(250),
	country VARCHAR(50),
	city VARCHAR(50)
);

/*
	The following query creates a table Employee.
    It contains personal information of each employees
    as columns.
	
*/
create table Employee (
	id INT AUTO_INCREMENT Primary Key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title VARCHAR(11),
	department int,
	email VARCHAR(50),
	country VARCHAR(50),
	city VARCHAR(50),
	location INT
);

/*
	The following query  gives the Employee table
    a reference for two columns (licenseID, DepartmentsID)
*/

alter table Employee
  add foreign key (location)
  references Locations(id);
  
alter table Employee
  add foreign key (department)
  references Departments(id);
 
 
/*
	The following query creates a table Computer.
    It has two columns which are the ID and its location.
*/

create table Computer(
	ID int AUTO_INCREMENT primary key,
	location INT
);

/*
	The following query alters a table Department.
    It references the locationsID from the Location table
*/

alter table Computer
	add foreign key(location)
    references Locations(id);

/*
	The following query creates a table License.
    It has columns of all the information around 
    particular software licenses
*/

create table License(
	id INT auto_increment Primary Key,
	licenseName VARCHAR(40),
	version VARCHAR(8),
	dateAdded date,
	licenseType VARCHAR(20),
	uploaderID INT
    
);

/*
	The following query alters the License table.
    It has references the Employee table and gets
    the EmployeesID
*/

alter table License
	add foreign key(uploaderID)
    references Employee(id);
    

/*
	The following query creates a table EmployeeAssign.
    It has ID and name as columns
*/
    
create table EmployeeAssign(
	id INT AUTO_INCREMENT Primary Key,
	licenseID INT,
    employeeID INT,
    assignerID INT,
    
    foreign key(licenseID) references License(id) ON DELETE CASCADE,
    foreign key(employeeID) references Employee(id),
    foreign key(assignerID) references Employee(id)
    
);

create table CompAssign(
	ID INT AUTO_INCREMENT Primary Key,
	licenseID INT,
    computerID INT,
    assignerID INT,
    
    foreign key(licenseID) references License(id) ON DELETE CASCADE,
    foreign key(computerID) references Computer(id),
    foreign key(assignerID) references Employee(id)
    
);


create table Cost(
	ID INT AUTO_INCREMENT Primary Key,
	licenseID INT,
    price decimal(10,2) NOT NULL,
    currency CHAR(3),
    period VARCHAR (12),
    renewalDate date, 
    
    foreign key(licenseID) references License(id) ON DELETE CASCADE
    
);

create table ExpirationDate(
	id INT AUTO_INCREMENT Primary Key,
	licenseID int,
    endDate date,
    
    foreign key(licenseID) references License(id) ON DELETE CASCADE
    
);


create table GeogRestriction(
	id INT AUTO_INCREMENT Primary Key,
	licenseID int,
    restriction VARCHAR(100),
    
    foreign key(licenseID) references License(id) ON DELETE CASCADE
    
);


  
