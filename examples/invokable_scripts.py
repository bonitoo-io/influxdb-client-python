"""
This example is related to `InfluxDB Cloud <https://docs.influxdata.com/influxdb/cloud/>`_ and not available
on a local InfluxDB OSS instance.

How to use Invokable scripts Cloud API to create custom endpoints that query data
"""
import datetime

from influxdb_client import InfluxDBClient, ScriptCreateRequest, ScriptLanguage, \
    ScriptUpdateRequest, Point
from influxdb_client.client.write_api import SYNCHRONOUS

"""
Define credentials
"""
influx_cloud_url = 'https://us-west-2-1.aws.cloud2.influxdata.com'
influx_cloud_token = '...'
bucket_name = '...'
org_name = '...'

with InfluxDBClient(url=influx_cloud_url, token=influx_cloud_token, org=org_name, debug=False,
                    timeout=20_000) as client:
    uniqueId = str(datetime.datetime.now())

    """
    Prepare data
    """
    _point1 = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
    _point2 = Point("my_measurement").tag("location", "New York").field("temperature", 24.3)
    client.write_api(write_options=SYNCHRONOUS).write(bucket=bucket_name, record=[_point1, _point2])

    scripts_api = client.invokable_scripts_api()

    """
    Create Invokable Script
    """
    print(f"------- Create -------\n")
    create_request = ScriptCreateRequest(name=f"my_script_{uniqueId}",
                                         description="my first try",
                                         language=ScriptLanguage.FLUX,
                                         script=f"from(bucket: params.bucket_name) |> range(start: -30d) |> limit(n:2)")

    created_script = scripts_api.create_script(create_request=create_request)
    print(created_script)

    """
    Update Invokable Script
    """
    print(f"------- Update -------\n")
    update_request = ScriptUpdateRequest(description="my updated description")
    created_script = scripts_api.update_script(script_id=created_script.id, update_request=update_request)
    print(created_script)

    """
    Invoke a script
    """
    # FluxRecords
    print(f"\n------- Invoke to FluxRecords -------\n")
    tables = scripts_api.invoke_script(script_id=created_script.id, params={"bucket_name": bucket_name})
    for table in tables:
        for record in table.records:
            print(f'FluxRecord {record}')
    # Pandas DataFrame
    print(f"\n------- Invoke to PandasData Frame -------\n")
    data_frame = scripts_api.invoke_script_data_frame(script_id=created_script.id, params={"bucket_name": bucket_name})
    print(data_frame.to_string())
    # CSV
    print(f"\n------- Invoke to CSV-------\n")
    csv_lines = scripts_api.invoke_script_csv(script_id=created_script.id, params={"bucket_name": bucket_name})
    for csv_line in csv_lines:
        if not len(csv_line) == 0:
            print(f'CSV row: {csv_line}')
    # RAW
    print(f"\n------- Invoke to Raw-------\n")
    raw = scripts_api.invoke_script_raw(script_id=created_script.id, params={"bucket_name": bucket_name})
    print(f'RAW output:\n {raw}')

    """
    List scripts
    """
    print(f"\n------- List -------\n")
    scripts = scripts_api.find_scripts()
    print("\n".join([f" ---\n ID: {it.id}\n Name: {it.name}\n Description: {it.description}" for it in scripts]))
    print("---")

    """
    Delete previously created Script
    """
    print(f"------- Delete -------\n")
    scripts_api.delete_script(script_id=created_script.id)
    print(f" Successfully deleted script: '{created_script.name}'")
