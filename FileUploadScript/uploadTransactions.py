import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

try:
    local_file_name = "C:/Users/Alex/Desktop/Budget/Transactions_2021_01_24_14_56_08.csv"
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client("transactions", blob="Transactions_2021_01_24_14_56_08.csv")

    with open(local_file_name, "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)