API and Usage
=============

SALTS uses a REST API to handle user requests.

Adding a License
----------------

To add a license, an HTTP POST request must be sent to the following URI: /addLicenses/

The request must include a ``Bearer`` field in the header with a valid authentication token indicating that the current user is a manager of the IT or Legal departments, as well as a JSON object in the body in the following format::

   {
     "name": <str>, //the name of the software, e.g. "Microsoft Office"
	 "ver": <str>, //the specific version of the software, e.g. "2.0.56"
	 "type": <str>, //the type of license, e.g. "Enterprise"
	 "cost": <float>, //the cost value for the license, e.g. 199.99
	 "curr": <str, 3 chars> //the currency that the cost value is in, e.g. "USD"
	 "period": <str>, //the renewal period for the license, e.g. "Annual"
	 "date_of_renewal": <str, yyyy-mm-dd>, //the date the license most recently renewed, e.g. "2025-06-30"
	 "expiration_date": <str, yyyy-mm-dd>, //the expiration date for the license, e.g. "2026-03-31"
	 "restrictions": <str> //a list of regions the license can't be used, e.g. "Croatia, Czech Republic"
   }

Definitions of each of these fields are as follows:

:name: The name of the software, e.g. "Microsoft Office" or "Mozilla Firefox"
