User Guide
==========

.. contents::
   :local:

Query
^^^^^
.. include:: ../README.rst
  :start-after: marker-query-start
  :end-before: marker-query-end

Write
^^^^^
.. include:: ../README.rst
  :start-after: marker-writes-start
  :end-before: marker-writes-end

Pandas DataFrame
^^^^^^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-pandas-start
  :end-before: marker-pandas-end

Delete data
^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-delete-start
  :end-before: marker-delete-end

Gzip support
^^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-gzip-start
  :end-before: marker-gzip-end

Proxy configuration
^^^^^^^^^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-proxy-start
  :end-before: marker-proxy-end

Nanosecond precision
^^^^^^^^^^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-nanosecond-start
  :end-before: marker-nanosecond-end

Handling Errors
^^^^^^^^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-handling-errors-start
  :end-before: marker-handling-errors-end

Debugging
^^^^^^^^^

For debug purpose you can enable verbose logging of http requests.
Both request header and body will be logged to standard output.

.. code-block:: python

    _client = InfluxDBClient(url="http://localhost:8086", token="my-token", debug=True, org="my-org")

Examples
^^^^^^^^
.. include:: ../README.rst
  :start-after: marker-examples-start
  :end-before: marker-examples-end