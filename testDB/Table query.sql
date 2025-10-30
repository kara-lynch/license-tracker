drop table if exists Departments, Computer, Employee, 
License, Locations, Cost, EmployeeAssign, ExpirationDate, 
GeogRestriction, CompAssign;

create table Departments (
	ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50)
);

create table Locations (
	id INT Primary Key,
	phone VARCHAR(50),
	street VARCHAR(250),
	country VARCHAR(50),
	city VARCHAR(50)
);

create table Employee (
	id INT Primary Key,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title VARCHAR(11),
	department int,
	email VARCHAR(50),
	country VARCHAR(50),
	city VARCHAR(50),
	location INT
);
alter table Employee
  add foreign key (location)
  references Locations(id);
  
alter table Employee
  add foreign key (department)
  references Departments(id);
  
create table Computer(
	ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	location INT
);

alter table Computer
	add foreign key(location)
    references Locations(id);

  
create table License(
	id INT Primary Key,
	licenseName VARCHAR(40),
	version VARCHAR(8),
	dateAdded date,
	licenseType VARCHAR(20),
	uploaderID INT
    
);

alter table License
	add foreign key(uploaderID)
    references Employee(id);
    
create table EmployeeAssign(
	id INT Primary Key,
	licenseID INT,
    employeeID INT,
    assignerID INT,
    
    foreign key(licenseID) references License(id),
    foreign key(employeeID) references Employee(id),
    foreign key(assignerID) references Employee(id)
    
);

create table CompAssign(
	ID INT Primary Key,
	licenseID INT,
    computerID INT,
    assignerID INT,
    
    foreign key(licenseID) references License(id),
    foreign key(computerID) references Computer(id),
    foreign key(assignerID) references Employee(id)
    
);


create table Cost(
	ID INT Primary Key,
	licenseID INT,
    price decimal(10,2) NOT NULL,
    currency CHAR(3),
    period VARCHAR (12),
    renewalDate date, 
    
    foreign key(licenseID) references License(id)
    
);

create table ExpirationDate(
	id INT Primary Key,
	licenseID int,
    endDate date,
    
    foreign key(licenseID) references License(id)
    
);


create table GeogRestriction(
	id INT Primary Key,
	licenseID int,
    restriction VARCHAR(100),
    
    foreign key(licenseID) references License(id)
    
);
  
