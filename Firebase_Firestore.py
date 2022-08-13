"""
SET UP THE FIRESTORE
open project settings --> Services accounts -- Copy `Admin SDK configuration snippet` and `Generate New Private Key`
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# import credentials file
cred = credentials.Certificate("YOUR CREDENTIALS FILE PATH")
firebase_admin.initialize_app(cred)

db = firestore.client()

"""         CREATE  DATA        """
# Create database with auto id
def add_data_auto_id(child, data):
    db.collection(child).add(data)

# Create databse with known id
def add_data_known_id(child,id,  data):
    db.collection(child).document(id).set(data)

# Merging data 
def merging_data_known_id(child,id,  data):
    db.collection(child).document(id).set(data, merge=True)

# Create new collection in child collection
def add_collection_into_child(child,id, child_2, data):
    db.collection(child).document(id).collection(child_2).add(data)

"""         READ DATA       """
# Read data with kown id
def get_data(child, id):
    data = db.collection(child).document(id).get()
    if data.exists:
        print(data.to_dict())

# Read all data
def get_all_data(child):
    data = db.collection(child).get()

    for each in data:
        print(each.to_dict())

# Read data with query
def get_all_data_query(child):
    data = db.collection('persons').where("age", ">=", 34).get()
  
    for each in data:
        print(each.to_dict())

"""         UPDATE  DATA        """
# update with known key
def update_data_key(child, key, data):
    db.collection(child).document(key).update(data)
"""
# update Increament
update_data_key('persons', 'nama_1', {'age': firestore.Increment(20)})
# update array
update_data_key('persons', 'nama_1', {'languages': firestore.ArrayUnion(['java'])})
# remove array
update_data_key('persons', 'nama_1', {'languages': firestore.ArrayRemove(['java'])})
"""

"""         DELETE  DATA        """
# delete with known document
def delete_document_key(child, key):
    db.collection(child).document(key).delete()

# delete with known field
def delete_field_key(child, key, data):
    db.collection(child).document(key).update({data : firestore.DELETE_FIELD})
