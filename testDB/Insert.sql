/*
Inserting data into Departments table
*/

INSERT INTO Departments (name) values('Sales');
INSERT INTO Departments (name) values('Information Technology');
INSERT INTO Departments (name) values('Legal');
INSERT INTO Departments (name) values('Hr');

/*
Inserting data into locations table
*/

insert into Locations (id, phone, street, country, city) values (1, '+81 664 654 5882', '384-1106, Yahara, Nerima-ku', 'Japan', 'Tokyo');
insert into Locations (id, phone, street, country, city) values (2, '+55 886 863 6908', 'Rua Atalaia 752', 'Brazil', 'SÃ£o Paulo');
insert into Locations (id, phone, street, country, city) values (3, '+1 334 275 3541', '3607 Fawn Valley Dr', 'United States', 'Dallas');
insert into Locations (id, phone, street, country, city) values (4, '+27 591 268 2006', '14, Jan Frederik Avenue', 'South Africa', 'Johnannesburg');
insert into Locations (id, phone, street, country, city) values (5, '+49 531 687 9657', '63, RÃ¶merweg', 'Germany', 'Berlin');

/*
Inserting test data into Employee table
*/

insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (1, 'Kasper', 'Gasnell', 'Sales Agent', 1, 'Kasper.Gasnell@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paul', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (2, 'Kennan', 'Duckworth', 'Developer', 2, 'Kennan.Duckworth@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (3, 'Lauren', 'Chambers', 'Developer', 2, 'Lauren.Chambers@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (4, 'Ardys', 'Picton', 'Developer', 2, 'Ardys.Picton@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (5, 'Brand', 'Napolitano', 'Developer', 2, 'Brand.Napolitano@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (6, 'Vevay', 'Petch', 'Developer', 2, 'Vevay.Petch@BuzzwordSolutions.com', 'Japan', 'Tokyo', 1);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (7, 'Prudi', 'Jaume', 'Aide', 3, 'Prudi.Jaume@BuzzwordSolutions.com', 'United States', 'Dallas', 3);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (8, 'Basil', 'Stennings', 'Developer', 2, 'Basil.Stennings@BuzzwordSolutions.com', 'United States', 'Dallas', 3);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (9, 'Harlene', 'Casaccia', 'Developer', 2, 'Harlene.Casaccia@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (10, 'Briana', 'Pitceathly', 'Developer', 2, 'Briana.Pitceathly@BuzzwordSolutions.com', 'United States', 'Dallas', 3);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (11, 'Temp', 'Wilsdon', 'Developer', 2, 'Temp.Wilsdon@BuzzwordSolutions.com', 'United States', 'Dallas', 3);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (12, 'Lee', 'Ewert', 'Developer', 2, 'Lee.Ewert@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (13, 'Theodora', 'Furphy', 'Aide', 3, 'Theodora.Furphy@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (14, 'Farr', 'Savage', 'Sales Agent', 1, 'Farr.Savage@BuzzwordSolutions.com', 'United States', 'Dallas', 3);
insert into Employee (id, first_name, last_name, title, department,  email, country, city, location) values (15, 'Agnola', 'Arran', 'Developer', 2, 'Agnola.Arran@BuzzwordSolutions.com', 'Brazil', 'SÃ£o Paulo', 2);

/*
Insert into computer table
*/

insert into Computer (id, location) values (1, 1);
insert into Computer (id, location) values (2, 2);
insert into Computer (id, location) values (3, 1);
insert into Computer (id, location) values (4, 1);
insert into Computer (id, location) values (5, 5);
insert into Computer (id, location) values (6, 3);
insert into Computer (id, location) values (7, 2);
insert into Computer (id, location) values (8, 3);
insert into Computer (id, location) values (9, 4);
insert into Computer (id, location) values (10, 1);

/*
Insert into the license table
*/

insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (1, 'Single User License', 'v2.1', '2012-04-16', 'Class A', 6);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (2, 'Multi-User License', 'v3.0', '2006-02-18', 'Class B', 4);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (3, 'Multi-User License', 'v3.0', '2016-02-22', 'Class B', 12);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (4, 'Enterprise License', 'v2.0', '2004-12-14', 'Class B', 3);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (5, 'Single User License', 'v3.0', '2011-04-07', 'Class C', 2);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (6, 'Single User License', 'v2.1', '2009-12-08', 'Class A', 5);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (7, 'Multi-User License', 'v1.1', '2008-05-30', 'Class B', 1);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (8, 'Enterprise License', 'v2.0', '2000-06-16', 'Class C', 5);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (9, 'Multi-User License', 'v2.0', '2006-02-25', 'Class A', 14);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (10, 'Enterprise License', 'v3.0', '2014-03-05', 'Class C', 8);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (11, 'Multi-User License', 'v2.0', '2015-08-03', 'Class A', 1);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (12, 'Enterprise License', 'v1.0', '2002-08-05', 'Class B', 3);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (13, 'Multi-User License', 'v3.0', '2021-09-13', 'Class C', 10);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (14, 'Single User License', 'v3.0', '2021-03-31', 'Class B', 11);
insert into License (id, licenseName, version, dateAdded, licenseType, uploaderID) values (15, 'Single User License', 'v3.0', '2014-09-19', 'Class B', 10);


/*
Insert into the EmployeeAssign
*/

insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (1, 6, 10, 2);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (2, 4, 5, 5);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (3, 5, 13, 10);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (4, 1, 9, 6);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (5, 1, 7, 7);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (6, 6, 10, 9);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (7, 3, 8, 12);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (8, 8, 14, 3);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (9, 1, 10, 7);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (10, 11, 1, 5);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (11, 10, 5, 9);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (12, 15, 8, 6);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (13, 3, 10, 7);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (14, 15, 9, 13);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (15, 11, 9, 13);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (16, 7, 10, 4);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (17, 4, 6, 3);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (18, 15, 9, 13);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (19, 1, 2, 13);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (20, 12, 14, 11);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (21, 5, 3, 3);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (22, 1, 3, 14);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (23, 5, 6, 8);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (24, 15, 7, 8);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (25, 8, 4, 11);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (26, 10, 12, 8);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (27, 12, 6, 7);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (28, 5, 5, 6);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (29, 7, 1, 10);
insert into EmployeeAssign (id, licenseID, employeeID, assignerID) values (30, 13, 2, 7);

/*
Insert into the CompAssign table
*/

insert into CompAssign (id, licenseID, computerID, assignerID) values (1, 2, 1, 15);
insert into CompAssign (id, licenseID, computerID, assignerID) values (2, 7, 3, 8);
insert into CompAssign (id, licenseID, computerID, assignerID) values (3, 4, 10, 6);
insert into CompAssign (id, licenseID, computerID, assignerID) values (4, 14, 6, 5);
insert into CompAssign (id, licenseID, computerID, assignerID) values (5, 10, 6, 4);
insert into CompAssign (id, licenseID, computerID, assignerID) values (6, 12, 3, 10);
insert into CompAssign (id, licenseID, computerID, assignerID) values (7, 12, 4, 4);
insert into CompAssign (id, licenseID, computerID, assignerID) values (8, 3, 7, 3);
insert into CompAssign (id, licenseID, computerID, assignerID) values (9, 10, 3, 6);
insert into CompAssign (id, licenseID, computerID, assignerID) values (10, 1, 2, 9);

/*
Insert into the Cost
*/

insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (1, 1, 7849.82, 'PLN', 'quarterly', '2000-07-03');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (2, 10, 3940.69, 'EUR', 'quarterly', '2021-08-11');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (4, 8, 507.57, 'CNY', 'bi-annual', '2017-02-28');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (5, 9, 513.31, 'CZK', 'annual', '2021-04-29');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (6, 15, 4942.93, 'THB', 'semi-annual', '2004-09-14');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (7, 7, 9898.61, 'EUR', 'quarterly', '2001-02-16');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (8, 2, 8131.64, 'PHP', 'quarterly', '2005-06-07');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (9, 3, 4285.48, 'EUR', 'monthly', '2006-12-05');
insert into Cost (ID, licenseID, price, currency, period, renewalDate) values (10, 4, 2580.44, 'PYG', 'semi-annual', '2021-09-16');

/*
Insert into ExpirationDate
*/

insert into ExpirationDate (id, licenseID, endDate) values (1, 4, '2009-06-12');
insert into ExpirationDate (id, licenseID, endDate) values (2, 2, '2000-01-12');
insert into ExpirationDate (id, licenseID, endDate) values (3, 8, '2020-08-29');
insert into ExpirationDate (id, licenseID, endDate) values (4, 3, '2003-07-01');
insert into ExpirationDate (id, licenseID, endDate) values (5, 7, '2000-04-23');
insert into ExpirationDate (id, licenseID, endDate) values (6, 6, '2013-04-15');
insert into ExpirationDate (id, licenseID, endDate) values (7, 1, '2002-02-25');
insert into ExpirationDate (id, licenseID, endDate) values (8, 12, '2004-06-13');
insert into ExpirationDate (id, licenseID, endDate) values (9, 10, '2018-03-08');
insert into ExpirationDate (id, licenseID, endDate) values (10, 5, '2017-09-04');

/*
Insert into GeogRestriction
*/

insert into GeogRestriction (id, licenseID, restriction) values (1, 11, 'Germany');
insert into GeogRestriction (id, licenseID, restriction) values (2, 3, 'Brazil');
insert into GeogRestriction (id, licenseID, restriction) values (3, 14, 'Brazil');
insert into GeogRestriction (id, licenseID, restriction) values (4, 4, 'Australia');
insert into GeogRestriction (id, licenseID, restriction) values (5, 9, 'USA');
insert into GeogRestriction (id, licenseID, restriction) values (6, 13, 'USA');
insert into GeogRestriction (id, licenseID, restriction) values (7, 1, 'USA');
insert into GeogRestriction (id, licenseID, restriction) values (8, 15, 'USA');
insert into GeogRestriction (id, licenseID, restriction) values (9, 10, 'Canada');
insert into GeogRestriction (id, licenseID, restriction) values (10, 12, 'Australia');


INSERT INTO License (licenseName, version, dateAdded, licenseType, uploaderID)
VALUES ('Windows', 'v1.0.1', '2025-11-04', 'Ent', 1);












