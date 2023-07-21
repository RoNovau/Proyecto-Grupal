from google.cloud import storage
import requests
from datetime import datetime


def cargar_archivo_parquet(data, context):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    year_month = fecha_actual.strftime('%Y-%m')

    # Generar los enlaces de los archivos Parquet
    yellow_tripdata_url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year_month}.parquet'
    green_tripdata_url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year_month}.parquet'

    # Descargar el archivo Parquet (yellow_tripdata)
    response_yellow = requests.get(yellow_tripdata_url)
    yellow_tripdata_content = response_yellow.content

    # Subir el archivo Parquet (yellow_tripdata) a Google Cloud Storage
    bucket_name = 'web_scraping_trips_0'
    blob_name_yellow = f'yellow_tripdata_{year_month}.parquet'
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob_yellow = bucket.blob(blob_name_yellow)
    blob_yellow.upload_from_string(yellow_tripdata_content, content_type='application/octet-stream')

    # Descargar el archivo Parquet (green_tripdata)
    response_green = requests.get(green_tripdata_url)
    green_tripdata_content = response_green.content

    # Subir el archivo Parquet (green_tripdata) a Google Cloud Storage
    blob_name_green = f'green_tripdata_{year_month}.parquet'
    blob_green = bucket.blob(blob_name_green)
    blob_green.upload_from_string(green_tripdata_content, content_type='application/octet-stream')