"""
Use API invokable scripts to create custom InfluxDB API endpoints that query, process, and shape data.

API invokable scripts let you assign scripts to API endpoints and then execute them as standard REST operations
in InfluxDB Cloud.
"""

from typing import List, Iterator, Generator, Any

from influxdb_client import Script, InvokableScriptsService, ScriptCreateRequest, ScriptUpdateRequest, \
    ScriptInvocationParams
from influxdb_client.client._base import _BaseQueryApi
from influxdb_client.client.flux_csv_parser import FluxResponseMetadataMode
from influxdb_client.client.flux_table import FluxRecord, TableList, CSVIterator


class InvokableScriptsApi(_BaseQueryApi):
    """Use API invokable scripts to create custom InfluxDB API endpoints that query, process, and shape data."""

    def __init__(self, influxdb_client):
        """Initialize defaults."""
        self._influxdb_client = influxdb_client
        self._invokable_scripts_service = InvokableScriptsService(influxdb_client.api_client)

    def create_script(self, create_request: ScriptCreateRequest) -> Script:
        """Create a script.

        :param ScriptCreateRequest create_request: The script to create. (required)
        :return: The created script.
        """
        return self._invokable_scripts_service.post_scripts(script_create_request=create_request)

    def update_script(self, script_id: str, update_request: ScriptUpdateRequest) -> Script:
        """Update a script.

        :param str script_id: The ID of the script to update. (required)
        :param ScriptUpdateRequest update_request: Script updates to apply (required)
        :return: The updated.
        """
        return self._invokable_scripts_service.patch_scripts_id(script_id=script_id,
                                                                script_update_request=update_request)

    def delete_script(self, script_id: str) -> None:
        """Delete a script.

        :param str script_id: The ID of the script to delete. (required)
        :return: None
        """
        self._invokable_scripts_service.delete_scripts_id(script_id=script_id)

    def find_scripts(self, **kwargs):
        """List scripts.

        :key int limit: The number of scripts to return.
        :key int offset: The offset for pagination.
        :return: List of scripts.
        :rtype: list[Script]
        """
        return self._invokable_scripts_service.get_scripts(**kwargs).scripts

    def invoke_script(self, script_id: str, params: dict = None) -> TableList:
        """
        Invoke synchronously a script and return result as a TableList.

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param params: bind parameters
        :return: List of FluxTable.
        :rtype: TableList
        """
        response = self._invokable_scripts_service \
            .post_scripts_id_invoke(script_id=script_id,
                                    script_invocation_params=ScriptInvocationParams(params=params),
                                    async_req=False,
                                    _preload_content=False,
                                    _return_http_data_only=False)
        return self._to_tables(response, query_options=None, response_metadata_mode=FluxResponseMetadataMode.only_names)

    def invoke_script_stream(self, script_id: str, params: dict = None) -> Generator['FluxRecord', Any, None]:
        """
        Invoke synchronously a script and return result as a Generator['FluxRecord'].

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param params: bind parameters
        :return: Stream of FluxRecord.
        :rtype: Generator['FluxRecord']
        """
        response = self._invokable_scripts_service \
            .post_scripts_id_invoke(script_id=script_id,
                                    script_invocation_params=ScriptInvocationParams(params=params),
                                    async_req=False,
                                    _preload_content=False,
                                    _return_http_data_only=False)

        return self._to_flux_record_stream(response, query_options=None,
                                           response_metadata_mode=FluxResponseMetadataMode.only_names)

    def invoke_script_data_frame(self, script_id: str, params: dict = None, data_frame_index: List[str] = None):
        """
        Invoke synchronously a script and return Pandas DataFrame.

        Note that if a script returns tables with differing schemas than the client generates
        a DataFrame for each of them.

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param List[str] data_frame_index: The list of columns that are used as DataFrame index.
        :param params: bind parameters
        :return: Pandas DataFrame.
        """
        _generator = self.invoke_script_data_frame_stream(script_id=script_id,
                                                          params=params,
                                                          data_frame_index=data_frame_index)
        return self._to_data_frames(_generator)

    def invoke_script_data_frame_stream(self, script_id: str, params: dict = None, data_frame_index: List[str] = None):
        """
        Invoke synchronously a script and return stream of Pandas DataFrame as a Generator['pd.DataFrame'].

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param List[str] data_frame_index: The list of columns that are used as DataFrame index.
        :param params: bind parameters
        :return: Stream of Pandas DataFrames.
        :rtype: Generator['pd.DataFrame']
        """
        response = self._invokable_scripts_service \
            .post_scripts_id_invoke(script_id=script_id,
                                    script_invocation_params=ScriptInvocationParams(params=params),
                                    async_req=False,
                                    _preload_content=False,
                                    _return_http_data_only=False)

        return self._to_data_frame_stream(data_frame_index, response, query_options=None,
                                          response_metadata_mode=FluxResponseMetadataMode.only_names)

    def invoke_script_csv(self, script_id: str, params: dict = None) -> CSVIterator:
        """
        Invoke synchronously a script and return result as a CSV iterator. Each iteration returns a row of the CSV file.

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param params: bind parameters
        :return: :class:`~Iterator[List[str]]` wrapped into :class:`~influxdb_client.client.flux_table.CSVIterator`
        """  # noqa: E501
        response = self._invokable_scripts_service \
            .post_scripts_id_invoke(script_id=script_id,
                                    script_invocation_params=ScriptInvocationParams(params=params),
                                    async_req=False,
                                    _preload_content=False)

        return self._to_csv(response)

    def invoke_script_raw(self, script_id: str, params: dict = None) -> Iterator[List[str]]:
        """
        Invoke synchronously a script and return result as raw unprocessed result as a str.

        The bind parameters referenced in the script are substitutes with `params` key-values sent in the request body.

        :param str script_id: The ID of the script to invoke. (required)
        :param params: bind parameters
        :return: Result as a str.
        """
        response = self._invokable_scripts_service \
            .post_scripts_id_invoke(script_id=script_id,
                                    script_invocation_params=ScriptInvocationParams(params=params),
                                    async_req=False,
                                    _preload_content=True)

        return response
