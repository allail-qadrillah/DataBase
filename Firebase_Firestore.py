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
def add_data_auto_id(collection, data):
    db.collection(collection).add(data)

# Create databse with known id
def add_data_known_id(collection, id,  data):
    db.collection(collection).document(id).set(data)

# Merging data
def merging_data_known_id(collection, id,  data):
    db.collection(collection).document(id).set(data, merge=True)

# Create new collection in collection collection
def add_collection_into_collection(collection, id, collection_2, data):
    db.collection(collection).document(id).collection(collection_2).add(data)


"""         READ DATA       """
# Read data with kown id
def get_data(collection, id):
    data = db.collection(collection).document(id).get()
    if data.exists:
        print(data.to_dict())

# Read all data
def get_all_data(collection):
    data = db.collection(collection).get()

    for each in data:
        print(each.to_dict())

# Read data with query
def get_all_data_query(collection):
    data = db.collection('persons').where("age", ">=", 34).get()

    for each in data:
        print(each.to_dict())


"""         UPDATE  DATA        """
# update with known key
def update_data_key(collection, key, data):
    db.collection(collection).document(key).update(data)

# update Increament
update_data_key('persons', 'nama_1', {'age': firestore.Increment(20)})
# update array
update_data_key('persons', 'nama_1', {'languages': firestore.ArrayUnion(['java'])})
# remove array
update_data_key('persons', 'nama_1', {'languages': firestore.ArrayRemove(['java'])})


"""         DELETE  DATA        """
# delete with known document
def delete_document_key(collection, key):
    db.collection(collection).document(key).delete()

# delete with known field
def delete_field_key(collection, key, data):
    db.collection(collection).document(key).update({data: firestore.DELETE_FIELD})
    
# delete data with look id in document 
def delete_data_with_id_document():
    # check id
    data = db.collection("data_employees").where('id', '==', id).get()
    # delete document id
    db.collection(collection).document(data[0].id).delete()
    
