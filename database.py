from pymongo import MongoClient, errors
from bson import ObjectId

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "testdb"
COLLECTION_NAME = "items"

# Create a MongoDB client
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
except errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    raise Exception(f"Could not connect to MongoDB: {e}")

def create_item(item):
    try:
        result = collection.insert_one(item)
        return result.inserted_id
    except errors.PyMongoError as e:
        print(f"An error occurred while creating the item: {e}")
        raise Exception(f"An error occurred while creating the item: {e}")

def read_item(filter):
    try:
        item = collection.find_one(filter)
        if item:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string
        return item
    except errors.PyMongoError as e:
        print(f"An error occurred while reading the item: {e}")
        raise Exception(f"An error occurred while reading the item: {e}")

def read_all_items():
    try:
        items = collection.find()
        items = [{**item, '_id': str(item['_id'])} for item in items]  # Convert ObjectId to string
        return items
    except errors.PyMongoError as e:
        print(f"An error occurred while reading all items: {e}")
        raise Exception(f"An error occurred while reading all items: {e}")

def update_item(filter, update):
    try:
        result = collection.update_one(filter, {'$set': update})
        return result.modified_count
    except errors.PyMongoError as e:
        print(f"An error occurred while updating the item: {e}")
        raise Exception(f"An error occurred while updating the item: {e}")

def delete_item(filter):
    try:
        result = collection.delete_one(filter)
        return result.deleted_count
    except errors.PyMongoError as e:
        print(f"An error occurred while deleting the item: {e}")
        raise Exception(f"An error occurred while deleting the item: {e}")
