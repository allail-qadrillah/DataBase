import pyrebase

firebase_config = {"YOUR FIREBASE CONFIG"} # get firebaseconfig == settungs -> project settings -- scroldown -- SDK setup and configuration

# Initialize app
firebase = pyrebase.initialize_app(firebase_config)

# Create variabel to store Build of Firebase
db = firebase.database()

# REAL TIME DATABASE
# CREATE data with random object
def create_data_push(data):
    db.push(data)
    print('Data pushed successfully')
# CREATE data with specify object
def create_data_set(data):
    db.child('people').push(data)
    print('Data seted successfully')

# UPDATE data 
def update_data(data, child_1, child_2):
    db.child(child_1).child(child_2).update(data)
    print('Data updated successfully')

# DELETE data 
def delete_data(data, child_1, child_2):
    db.child(child_1).child(child_2).remove()
    print('Data deleted successfully')

# READ data 
def read_data(child):
    data = db.child(child).get()
    for each in data.each():
        print(each.val())
# READ data with specified indexes
# Realtime Database -> Rules == "child" : ["key"]
def read_data_specified(child, key, val):
    data = db.child(child).order_by_child(key).equal_to(val).get()
    for each in data.each():
        print(each.val())

