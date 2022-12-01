"""
USING FIREBASE ADMIN SDK
https://geekscoders.com/courses/python-firebase/lessons/python-firebase-admin-sdk-with-realtime-database/
"""
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://firepro-c07de.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
    'Employee':
        {
            'emp1': {
                'name':'Parwiz',
                'lname':'Forogh',
                'age':24
            },
            'emp2': {
                'name':'John',
                'lname':'Doe',
                'age':20
             }
        }
})
#updating data
ref = db.reference('Employee')
emp_ref = ref.child('emp1')
emp_ref.update({
    'name':'Python'
})
#multiple update
ref = db.reference('Employee')
ref.update({
    'emp1/lname':'updated lname1',
    'emp2/lname':'updated lname2'
})
#adding value using push
ref = db.reference('Employee2')
emp_ref = ref.push({
    'name':'Bob',
    'lname':'Logan',
    'email':'bob@gmail.com',
    'age':24
 
 
})
print(emp_ref.key)
 
ref = db.reference('Employee2')
print(ref.get())

"""
USING PYREBASE
https://github.com/thisbejim/Pyrebase#database
"""
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

