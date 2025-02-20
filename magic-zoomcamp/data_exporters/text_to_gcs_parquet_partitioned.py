import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/personal-gcp.json/rare-inquiry-412603-a9afc3d760e0_google_credentials.json"

bucket_name = 'mage-zoomcamp-gtf'
project_id = 'rare-inquiry-412603'
table_name = 'nyc_taxi_data'

#object_key = 'nyc_taxi_data.parquet'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['tpep_pickup_date'],
        filesystem=gcs

    )

