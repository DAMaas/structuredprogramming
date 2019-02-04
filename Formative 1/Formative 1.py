import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['shopping']
collection = db['products']

# Tests

print("Collections:")
print(db.list_collection_names())