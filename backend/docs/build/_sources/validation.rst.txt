Validation Checks
=================

SALTS has several built-in validation checks to ensure that the data passed into it is valid. For example, the ``check_field_size`` function will raise a ``ValueError`` if its input is outside the specified bounds. These functions are used by the :doc:`credentials` object.

.. automodule:: src.validation.validation_checks
   :members: