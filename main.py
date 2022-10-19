from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import subprocess

default_credential = DefaultAzureCredential()

#client = BlobServiceClient('jan.holub@1pf.onmicrosoft.com', credential=default_credential)

try:
    result = subprocess.check_output('az account show',shell=True)
    print(result.decode('utf-8'))
except subprocess.CalledProcessError as e:
    print(e.output)
