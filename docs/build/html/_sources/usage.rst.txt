Usage
=====

Installation
------------

Deployment notes go here

User Credentials
----------------
SALTS has an object class, ``UserCredentials``, that handles the information for the current user.

.. automodule:: src.credentials.credentials_manager
   :members:

Validation Checks
-----------------

SALTS has several built-in validation checks to ensure that the data passed into it is valid. For example, the ``check_field_size`` function will raise a ``ValueError`` if its input is outside the specified bounds.

.. automodule:: src.validation.validation_checks
   :members:
   
