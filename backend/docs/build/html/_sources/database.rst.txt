Database Calls
==============
SALTS uses the ``LicenseDAO`` object to handle calls to the database.

.. py.class:: _LicenseDAO	
   LicenseDAO handles license-related operations in the database, including adding, deleting, searching for, and assigning licenses. It is designed to process user requests and enforce access control by validating user credentials before executing any database actions.
	
.. py.method:: src.database.record_entities_licenseID._LicenseDAO.__init__()
   Initializes the LicenseDAO instance by establishing a connection to the MySQL database.

   This method reads database credentials from a configuration file defined in ``Settings.db_config_file()``, and uses them to create a shared MySQL connection and cursor for executing queries.
	
   :param LicenseDAO.conn: A class-level MySQL connection object.
   :param LicenseDAO.cursor: A class-level cursor object for executing SQL statements.
   :param self.cursor: An instance-level reference to the shared cursor.
	
   :raise FileNotFoundError: If the configuration file cannot be found.
   :raise json.JSONDecodeError: If the configuration file is not valid JSON.
   :raise mysql.connector.Error: If the database connection fails.
	
.. py.method:: src.database.record_entities_licenseID._LicenseDAO.seeLicenses()
	Retrieves and compiles detailed license information from the database.

    This method performs a multi-table SQL query using LEFT JOINs to gather data from the ``License``, ``Cost``, ``ExpirationDate``, and ``GeogRestriction`` tables. It returns a dictionary of license records, keyed by license ID, with each record containing:

    - ``name``: License name
    - ``ver``: License version
    - ``type``: License type
    - ``cost``: License cost (float or None)
    - ``curr``: Currency of the cost
    - ``period``: Billing period
    - ``date_of_renewal``: Renewal date (formatted as YYYY-MM-DD or None)
    - ``expiration_date``: Expiration date (formatted as YYYY-MM-DD or None)
    - ``restrictions``: Geographic restrictions

    More information on these fields can be found on the :doc:`api` page.

    Note: If certain fields (e.g., cost, renewal date, expiration date) are missing, their values will be set to ``None``.
        
    :return: A dictionary of license records with structured metadata.
    :rtype: dict

