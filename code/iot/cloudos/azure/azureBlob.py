from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

def uploadToAzure(file_path_on_local, full_path_on_cloud):
    try:
        # Create the BlockBlobService that is used to call the Blob service for the storage account
        credential=ClientSecretCredential(
            client_id=env('client_id'),
            client_secret=env('client_secret'),
            tenant_id=env('tenant_id')
        )
        blob_service_client = BlobServiceClient(account_url="https://{}.blob.core.windows.net".format(env('storage_account_name')),
                                               credential=credential)

        container_name = env('container_name')
        blob_service_client.get_container_client(container_name)
        blob_service_client.get_blob_client(container=container_name, blob=full_path_on_cloud).upload_blob(file_path_on_local)
        print("File uploaded: {}".format(full_path_on_cloud))

    except Exception as e:
        print(e)