"""
Use API invokable scripts to create custom InfluxDB API endpoints that query, process, and shape data.

API invokable scripts let you assign scripts to API endpoints and then execute them as standard REST operations
in InfluxDB Cloud.
"""

from influxdb_client import Script, InvocableScriptsService, ScriptCreateRequest


class InvocableScriptsApi(object):
    """Use API invokable scripts to create custom InfluxDB API endpoints that query, process, and shape data."""

    def __init__(self, influxdb_client):
        """Initialize defaults."""
        self._influxdb_client = influxdb_client
        self._invocable_scripts_service = InvocableScriptsService(influxdb_client.api_client)

    def create_script(self, create_request: ScriptCreateRequest) -> Script:
        """Create a script.

        :param ScriptCreateRequest create_request: The script to create. (required)
        :return: The created script.
        """
        return self._invocable_scripts_service.post_scripts(script_create_request=create_request)
