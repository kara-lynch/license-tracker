Installation
============

Software required:

- Python 3.12+
- Flask 3.1.2
- MySQL 8.0.43

Python modules required:

- Requests
- Flask
- MySQL and MySQL Connector

SQL database structure:

- ``Employees``
	- ``id``: ``INT``
	- ``first_name``: ``VARCHAR(50)``
	- ``last_name``: ``VARCHAR(50)``
	- ``title``: ``VARCHAR(11)``
	- ``department``: ``INT``, foreign key (``Departments``)
	- ``email``: ``VARCHAR(50)``
	- ``country``: ``VARCHAR(50)``
	- ``city``: ``VARCHAR(50)``
	- ``location``: ``INT``, foreign key (``Locations``)
- ``Departments``
	- ``id``: ``INT``
	- ``name``: ``VARCHAR(50)``
- ``Locations``
	- ``id``: ``INT``
	- ``phone``: ``VARCHAR(50)``
	- ``street``: ``VARCHAR(250)``
	- ``country``: ``VARCHAR(50)``
	- ``city``: ``VARCHAR(50)``
- ``Computers``
	- ``id``: ``INT``
	- ``location``: ``INT``, foreign key (``Locations``)
- ``Licenses``
	- ``id``: ``INT``
	- ``licenseName``: ``VARCHAR(40)``
	- ``version``: ``VARCHAR(8)``
	- ``dateAdded``: ``DATE``
	- ``licenseType``: ``VARCHAR(20)``
	- ``uploaderID``: ``INT``, foreign key (``Employees``)
- ``Cost``
	- ``id``: ``INT``
	- ``licenseID``: ``INT``, foreign key (``Licenses``)
	- ``price``: ``FLOAT``
	- ``currency``: ``VARCHAR(3)``
	- ``period``: ``VARCHAR(12)``
	- ``renewalDate``: ``DATE``
- ``ExpirationDate``
	- ``id``: ``INT``
	- ``licenseID``: ``INT``, foreign key (``Licenses``)
	- ``endDate``: ``DATE``
- ``GeogRestrictions``
	- ``id``: ``INT``
	- ``licenseID``: ``INT``, foreign key (``Licenses``)
	- ``restrictions``: ``VARCHAR(100)``
- ``EmployeeAssign``
	- ``id``: ``INT``
	- ``licenseID``: ``INT``, foreign key (``Licenses``)
	- ``employeeID``: ``INT``, foreign key (``Employees``)
	- ``assignerID``: ``INT``, foreign key (``Employees``)
- ``ComputerAssign``
	- ``id``: ``INT``
	- ``licenseID``: ``INT``, foreign key (``Licenses``)
	- ``computerID``: ``INT``, foreign key (``Computers``)
	- ``assignerID``: ``INT``, foreign key (``Employees``)
   
Additional notes:

- Make sure ``logger.json`` is in ``/src/config/logger.json``.
- The URL for the authentication server is stored in ``/src/config/settings.json``.
- Database credentials are stored in ``/src/config/db_credentials.json``.

   
