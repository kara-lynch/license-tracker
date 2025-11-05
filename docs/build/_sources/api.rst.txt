API and Usage
=============

SALTS uses a REST API to handle user requests. It has four URIs that can be contacted.

Displaying the Documentation
----------------------------

To show this documentation page, an HTTP GET request can be sent to the following URI: ``/``

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
