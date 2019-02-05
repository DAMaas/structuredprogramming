import pymongo
from pymongo import MongoClient

# Initialize all variables needed to connect

address = "mongodb://localhost:27017/"

# Functions

# Get all databases from a running MongoDB instance
def getDatabases(address):
    client = MongoClient(address)
    databaseList = client.list_database_names()
    return databaseList

# Get all collections from a single database or all databases
def getCollections(database):
    client = MongoClient(address)
    collectionDict = {}
    # Is the passed database variable is a list
    if isinstance(database, list):
        for item in database:
            db = client[item]
            collectionDict[item] = db.list_collection_names()
        return collectionDict
    # If it is not a list
    else:
        db = client[database]
        collectionDict[database] = db.list_collection_names()
        return collectionDict

testDatabases = getDatabases(address)
print(testDatabases)

testCollectionsString = getCollections("shopping")
print(testCollectionsString)

testCollectionsDict = getCollections(testDatabases)
print(testCollectionsDict)