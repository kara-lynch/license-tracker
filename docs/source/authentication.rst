Authentication
==============
SALTS is built to use your organization's pre-existing authentication server and will query it for each request.

.. autoclass:: src.util.authenticate._Authenticate
   :private-members: _validate_token
   :members: authorize