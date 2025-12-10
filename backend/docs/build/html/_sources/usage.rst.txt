Installation
============

Software required:

- Python 3.12+
- Flask 3.1.2
- Docker 29.1.1
- MySQL Workbench 8.0.36

Python modules required:

- Requests
- Flask
- MySQL and MySQL Connector

To initialize the database:

- Run the Docker script located at ``docker/start_docker_db.sh``. This will create a Docker container running MySQL v8.0.43. You may want to edit the script to change the default root password first.
- Connect to the database using MySQL Workbench and run the SQL script located in ``backend/testDB/create_tables.sql`` in the database to initialize all of the tables. You may want to edit the script and change the default user credentials first.
- On the backend server, edit ``backend/src/config/db_credentials.json`` and add the credentials for both user accounts, as well as the IP for the database server. It should be in the following format::

	{
	  "manager-level": {
	    "host": "127.0.0.1", //IP for the DB server goes here
		"port": "3306",
		"username": "root",
		"password": "secretredteampw", //if you changed it, the root password goes here
		"database": "sys"
	  },
	  "employee-level": {
	    "host": "127.0.0.1", //IP for the DB server goes here
		"port": "3306",
		"username": "employee",
		"password": "notsosecretpw", //if you changed it, the employee password goes here
		"database": "sys"
	  }
	}
		

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

   
