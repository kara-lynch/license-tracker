API and Usage
=============

SALTS uses a REST API to handle user requests. It has four URIs that can be contacted.

Pinging the Server
----------------------------

To ensure the backend is online and working, an HTTP GET request can be sent to the following URI: ``/helloWorld/``

If everything is functional, the API will return an HTML page that says "Hello!"

Getting All Licenses
--------------------

To get a list of all licenses in the system, an HTTP GET request must be sent to the following URI: ``/seeLicenses/``

The request must include a ``Bearer`` field in the header with a valid authentication token. The records will be returned as a JSON object in the following format::

	{
		"<id>": {
			"name": <str>,
			"ver": <str>,
			"type": <str>,
			"cost": <float>,
			"curr": <str, 3 chars>,
			"period": <str>, 
			"date_of_renewal": <str, yyyy-mm-dd>,
			"expiration_date": <str, yyyy-mm-dd>,
			"restrictions": <str>
		},
		...
	}
	
All fields other than ``id``, ``name``, ``ver``, and ``type`` are optional and as such may not be present in every record. Definitions of each of these fields are as follows:

:id: The ID number automatically assigned to each license record.
:name: The name of the software, e.g. "Microsoft Office" or "Mozilla Firefox".
:ver:  The specific version of the software, e.g. "2.0.56".
:type: The type of license, e.g. "Enterprise" or "Open Source".
:cost: The cost value for the license, e.g. 199.99 or 15000.
:curr: The ISO three-letter code for the currency the cost value is in, e.g. "USD" or "GBP".
:period: The renewal period for the license, e.g. "Annual" or "Monthly".
:date_of_renewal: The date the license most recently renewed, e.g. "2025-06-30".
:expiration_date: The expiration date for the license, e.g. "2026-03-31".
:restrictions: A list of regions the license can't be used, e.g. "Croatia, Czech Republic" or "All countries except Japan".

Getting All Licenses in a Range
-------------------------------

To get a specific number of licenses in the system, an HTTP POST request must be sent to the following URI: ``/seeLicenseRange/``

The request must include a ``Bearer`` field in the header with a valid authentication token, as well as a JSON object in the body in the following format:: 

	{
	  "range": <int>,
	  "offset": <int>,
	  "sort_field": <str>,
	  "ascending": <bool>
	}
	
All fields other than ``range`` are optional. Definitions of each of these fields are as follows:

:range: The number of records to return.
:offset: The position in the order to start from. Defaults to 0. If specified, must be at least 1.
:sort_field: The database field to sort the records by. If not specified, the records will be sorted by ``licenseID``. If specified, must be one of the following: ``licenseName``, ``licenseType``, ``price``, ``period``, ``renewalDate``, ``endDate``, or ``restriction``.
:ascending: If ``True``, records will be sorted in ascending order. Defaults to ``False`` and is only used if ``sort_field`` is specified.

The records will be returned in the same format as seeing all of them. This is generally used for the infinite scrolling functionality built into the front end.

Adding a License
----------------

To add a license, an HTTP POST request must be sent to the following URI: ``/addLicenses/``

The request must include a ``Bearer`` field in the header with a valid authentication token indicating that the current user is a manager of the IT or Legal departments, as well as a JSON object in the body in the following format::

	{
	  "name": <str>,
	  "ver": <str>,
	  "type": <str>,
	  "cost": <float>,
	  "curr": <str, 3 chars>,
	  "period": <str>, 
	  "date_of_renewal": <str, yyyy-mm-dd>,
	  "expiration_date": <str, yyyy-mm-dd>,
	  "restrictions": <str>
	}

All fields other than ``name``, ``ver``, and ``type`` are optional. Definitions of each of these fields are as follows:

:name: The name of the software, e.g. "Microsoft Office" or "Mozilla Firefox".
:ver:  The specific version of the software, e.g. "2.0.56".
:type: The type of license, e.g. "Enterprise" or "Open Source".
:cost: The cost value for the license, e.g. 199.99 or 15000. If present, ``curr`` must also be defined.
:curr: The ISO three-letter code for the currency the cost value is in, e.g. "USD" or "GBP". If present, ``cost`` must also be defined.
:period: The renewal period for the license, e.g. "Annual" or "Monthly". If present, ``cost`` and ``curr`` must also be defined.
:date_of_renewal: The date the license most recently renewed, e.g. "2025-06-30". If present, ``cost`` and ``curr`` must also be defined.
:expiration_date: The expiration date for the license, e.g. "2026-03-31".
:restrictions: A list of regions the license can't be used, e.g. "Croatia, Czech Republic" or "All countries except Japan".

If the request is successful, the API will return an HTML page that says "License added."



Removing a License
------------------

To delete a license, an HTTP DELETE request must be sent to the following URI: ``/deleteLicense/``

The request must include a ``Bearer`` field in the header with a valid authentication token indicating that the current user is a manager of the IT or Legal departments, as well as a JSON object in the body in the following format::

	{
		"licenseID": <int>
	}
	
The ``licenseID`` field must include the ID number for the record you wish to remove. This ID can be obtained with a request to see all licenses, as described above.

If the request is successful, the API will return an HTML page that says "Record removed."

Assigning a License
-------------------
To assign a software license to an employee, an HTTP POST request must be sent to the following URI: ``/employeeAssign/``

The request must include a ``Bearer`` field in the header with a valid authentication token indicating that the current user is a manager of the IT or Legal departments, as well as a JSON object in the body in the following format::

	{
		"licenseID": <int>,
		"employeeID": <int>
	}
	
Definitions of each of these fields are as follows:
	
:licenseID: The ID number for the license to be assigned. This ID can be obtained with a request to see all licenses, as described above.
:employeeID: The ID number for the employee the license is being assigned to.

If the request is successful, the API will return an HTML page that says "License assigned".

Unassigning a License
---------------------
To remove a software assignment record, an HTTP DELETE request must be sent to the following URI: ``/employeeUnassign/``

The request must include a ``Bearer`` field in the header with a valid authentication token indicating that the current user is a manager of the IT or Legal departments, as well as a JSON object in the body in the following format::

	{
		"licenseID": <int>,
		"employeeID": <int>
	}
	
Definitions of each of these fields are as follows:
	
:licenseID: The ID number for the license to be assigned. This ID can be obtained with a request to see all licenses, as described above.
:employeeID: The ID number for the employee the license is being assigned to.

If the request is successful, the API will return an HTML page that says "License assignment removed".

Seeing License Assignments
--------------------------
To see all licenses that have been assigned to a user, an HTTP POST request must be sent to the following URI: ``/seeAssignment/``

The request must include a ``Bearer`` field in the header with a valid authentication token, as well as a JSON object in the body in the following format:: 

	{
	  "range": <int>,
	  "offset": <int>,
	  "sort_field": <str>,
	  "ascending": <bool>,
	  "employeeID": <int>
	}
	
All fields other than ``range`` are optional. Definitions of each of these fields are as follows:

:range: The number of records to return.
:offset: The position in the order to start from. Defaults to 0. If specified, must be at least 1.
:sort_field: The database field to sort the records by. If not specified, the records will be sorted by ``licenseID``. If specified, must be one of the following: ``licenseName``, ``licenseType``, ``price``, ``period``, ``renewalDate``, ``endDate``, or ``restriction``.
:ascending: If ``True``, records will be sorted in ascending order. Defaults to ``False`` and is only used if ``sort_field`` is specified.
:employeeID: If the current user is a manager of the IT or Legal departments, this field can be specified to look up all licenses assigned to the user with the specified ID. If the user does not have this authorization, or if this field is not specified, it defaults to the current user's ID.

The records will be returned in the same format as seeing all of them. This is generally used for the infinite scrolling functionality built into the front end.
