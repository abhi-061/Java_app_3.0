import requests

# Replace these variables with your own values
artifactory_url = 'http://54.176.142.237:8082/artifactory/example-repo-local/'
repository_name = 'example-repo-local'
username = 'admin'
password = 'Devadmin@123'
file_path ='/root/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

# Construct the API URL for uploading
upload_url = f'{artifactory_url}/{repository_name}/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

# Prepare the authentication credentials
auth = (username, password)

# Perform the file upload
with open(file_path, 'rb') as file:
    response = requests.put(upload_url, data=file, auth=auth)

if response.status_code == 201:
    print(f'Successfully uploaded {file_path} to {upload_url}')
else:
    print(f'Failed to upload {file_path}. Status code: {response.status_code}')
    print(response.text)
