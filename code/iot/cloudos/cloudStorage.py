from __future__ import absolute_import
import environ
from .azure.azureBlob import uploadToAzure
from .gcp.gcpBucket import uploadToGcp

env = environ.Env(
    DEBUG=(bool, False)
)

cloud_environment = env('cloud_environment')

def uploadToCloud(file_path_on_local, full_path_on_cloud):
    if cloud_environment == 'azure':
        uploadToAzure(file_path_on_local, full_path_on_cloud)
    elif cloud_environment == 'gcp':
        uploadToGcp(file_path_on_local, full_path_on_cloud)



