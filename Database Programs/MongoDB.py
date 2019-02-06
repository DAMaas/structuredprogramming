from pymongo import MongoClient
import json

# Initialize all variables needed to connect

address = "mongodb://localhost:27017/"

# Functions

def getDatabases(address):
    """
    Get all databases from a running MongoDB instance.

    Args:
        address: URI of the MongoDB instance. For example: "mongodb://localhost:27017/"

    Returns:
        databaseList: A list of all the databases
    """

    client = MongoClient(address)
    databaseList = client.list_database_names()
    return databaseList

def getCollections(database):
    """
    Get all collections from a or all databases in a running MongoDB instance.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"]

    Returns:
        collectionDict: A dictionary with the database as key and the collections as value.
    """
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

def readFiles():
    with open('/home/phoenix/Documents/School/Structured Programming/Projects/Structured Programming/Database Programs/test.json') as data_file:    
        data = json.load(data_file)
    return data

def getCollectionDocuments(database, collection):
    documentList = []
    client = MongoClient(address)
    client_db = client[database]
    client_db_collection = client_db[collection]
    document = client_db_collection.find()

    for item in document:
        documentList.append(item)
    return documentList

#databaseList = getDatabases(address)

#collectionDict = getCollections(databaseList)

#documentList = getCollectionDocuments("shopping", "products")

data = readFiles()
print(data)