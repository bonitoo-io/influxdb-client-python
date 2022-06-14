"""
Querying InfluxDB by FluxLang.

Flux is InfluxData’s functional data scripting language designed for querying, analyzing, and acting on data.
"""

from typing import List, Generator, Any, Callable

from influxdb_client import Dialect
from influxdb_client.client._base import _BaseQueryApi
from influxdb_client.client.flux_table import FluxRecord, TableList, CSVIterator


class QueryOptions(object):
    """Query options."""

    def __init__(self, profilers: List[str] = None, profiler_callback: Callable = None) -> None:
        """
        Initialize query options.

        :param profilers: list of enabled flux profilers
        :param profiler_callback: callback function return profilers (FluxRecord)
        """
        self.profilers = profilers
        self.profiler_callback = profiler_callback


class QueryApi(_BaseQueryApi):
    """Implementation for '/api/v2/query' endpoint."""

    def __init__(self, influxdb_client, query_options=QueryOptions()):
        """
        Initialize query client.

        :param influxdb_client: influxdb client
        """
        super().__init__(influxdb_client=influxdb_client, query_options=query_options)

    def query_csv(self, query: str, org=None, dialect: Dialect = _BaseQueryApi.default_dialect, params: dict = None) \
            -> CSVIterator:
        """
        Execute the Flux query and return results as a CSV iterator. Each iteration returns a row of the CSV file.

        :param query: a Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param dialect: csv dialect format
        :param params: bind parameters
        :return: :class:`~Iterator[List[str]]` wrapped into :class:`~influxdb_client.client.flux_table.CSVIterator`

        Serialization the query results to flattened list of values via :func:`~influxdb_client.client.flux_table.CSVIterator.to_values`:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using CSV iterator
                csv_iterator = client.query_api().query_csv('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to values
                output = csv_iterator.to_values()
                print(output)

        If you would like to turn off `Annotated CSV header's <https://docs.influxdata.com/influxdb/latest/reference/syntax/annotated-csv/>`_ you can use following code:

        .. code-block:: python

            from influxdb_client import InfluxDBClient, Dialect

            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using CSV iterator
                csv_iterator = client.query_api().query_csv('from(bucket:"my-bucket") |> range(start: -10m)',
                                                            dialect=Dialect(header=False, annotations=[]))

                for csv_line in csv_iterator:
                    print(csv_line)
        """  # noqa: E501
        org = self._org_param(org)
        response = self._query_api.post_query(org=org, query=self._create_query(query, dialect, params),
                                              async_req=False, _preload_content=False)

        return self._to_csv(response)

    def query_raw(self, query: str, org=None, dialect=_BaseQueryApi.default_dialect, params: dict = None):
        """
        Execute synchronous Flux query and return result as raw unprocessed result as a str.

        :param query: a Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param dialect: csv dialect format
        :param params: bind parameters
        :return: str
        """
        org = self._org_param(org)
        result = self._query_api.post_query(org=org, query=self._create_query(query, dialect, params), async_req=False,
                                            _preload_content=False)

        return result

    def query(self, query: str, org=None, params: dict = None) -> TableList:
        """Execute synchronous Flux query and return result as a :class:`~influxdb_client.client.flux_table.FluxTable` list.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param params: bind parameters
        :return: :class:`~influxdb_client.client.flux_table.FluxTable` list wrapped into
                 :class:`~influxdb_client.client.flux_table.TableList`

        Serialization the query results to flattened list of values via :func:`~influxdb_client.client.flux_table.TableList.to_values`:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using Table structure
                tables = client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to values
                output = tables.to_values(columns=['location', '_time', '_value'])
                print(output)

        Serialization the query results to JSON via :func:`~influxdb_client.client.flux_table.TableList.to_json`:

        .. code-block:: python

            from influxdb_client import InfluxDBClient

            with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org") as client:

                # Query: using Table structure
                tables = client.query_api().query('from(bucket:"my-bucket") |> range(start: -10m)')

                # Serialize to JSON
                output = tables.to_json(indent=5)
                print(output)
        """  # noqa: E501
        org = self._org_param(org)

        response = self._query_api.post_query(org=org, query=self._create_query(query, self.default_dialect, params),
                                              async_req=False, _preload_content=False, _return_http_data_only=False)

        return self._to_tables(response, query_options=self._get_query_options())

    def query_stream(self, query: str, org=None, params: dict = None) -> Generator['FluxRecord', Any, None]:
        """
        Execute synchronous Flux query and return stream of FluxRecord as a Generator['FluxRecord'].

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param params: bind parameters
        :return: Generator['FluxRecord']
        """
        org = self._org_param(org)

        response = self._query_api.post_query(org=org, query=self._create_query(query, self.default_dialect, params),
                                              async_req=False, _preload_content=False, _return_http_data_only=False)
        return self._to_flux_record_stream(response, query_options=self._get_query_options())

    def query_data_frame(self, query: str, org=None, data_frame_index: List[str] = None, params: dict = None):
        """
        Execute synchronous Flux query and return Pandas DataFrame.

        Note that if a query returns tables with differing schemas than the client generates
        a DataFrame for each of them.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param data_frame_index: the list of columns that are used as DataFrame index
        :param params: bind parameters
        :return: DataFrame or List of DataFrames
        """
        _generator = self.query_data_frame_stream(query, org=org, data_frame_index=data_frame_index, params=params)
        return self._to_data_frames(_generator)

    def query_data_frame_stream(self, query: str, org=None, data_frame_index: List[str] = None, params: dict = None):
        """
        Execute synchronous Flux query and return stream of Pandas DataFrame as a Generator['pd.DataFrame'].

        Note that if a query returns tables with differing schemas than the client generates
        a DataFrame for each of them.

        :param query: the Flux query
        :param str, Organization org: specifies the organization for executing the query;
                                      Take the ``ID``, ``Name`` or ``Organization``.
                                      If not specified the default value from ``InfluxDBClient.org`` is used.
        :param data_frame_index: the list of columns that are used as DataFrame index
        :param params: bind parameters
        :return:
        """
        org = self._org_param(org)

        response = self._query_api.post_query(org=org, query=self._create_query(query, self.default_dialect, params),
                                              async_req=False, _preload_content=False, _return_http_data_only=False)

        return self._to_data_frame_stream(data_frame_index=data_frame_index,
                                          response=response,
                                          query_options=self._get_query_options())

    def __del__(self):
        """Close QueryAPI."""
        pass
