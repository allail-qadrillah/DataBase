import pyrebase

firebase_config = {"YOUR FIREBASE CONFIG"} # get firebaseconfig == settungs -> project settings -- scroldown -- SDK setup and configuration

# Initialize app
firebase = pyrebase.initialize_app(firebase_config)

# Create variabel to store Build of Firebase
storage = firebase.storage()

# STORANGE
# upload files to cloud storage
def upload_files(filename, cloudFilename):
    storage.child(cloudFilename).put(filename)
    print('Uploading files to cloud storage successfully')

# get files url from cloud storage
def get_files_url(filename, cloudFilename):
    return storage.child(cloudFilename).get_url(None)
