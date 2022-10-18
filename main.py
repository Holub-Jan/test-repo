from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

default_credential = DefaultAzureCredential()

client = BlobServiceClient('jan.holub@1pf.onmicrosoft.com', credential=default_credential)

print(client)
