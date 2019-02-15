# Import dependencies

from pymongo import MongoClient
# import json # Might be needed for parsing data, stay tuned to find out if I get it to work
# import bson # Might be needed for parsing data, stay tuned to find out if I get it to work


# Initialize variables


address = "mongodb://localhost:27017/"


# Define functions


def getDatabases(address):
    """
    Get all databases from a running MongoDB instance.

    Args:
        address: URI of the MongoDB instance. For example: "mongodb://localhost:27017/".

    Returns:
        databaseList: A list of all the databases.
    """

    client = MongoClient(address)
    databaseList = client.list_database_names()
    return databaseList


def getCollections(address, database):
    """
    Get all collections from a or multiple database(s) in a running MongoDB instance.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"].

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


def getCollectionDocuments(address, database, collection):
    """
    Get all documents from a specific collection.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"].
        collection: String with the name of the collection. For example: "names" or "products".

    Returns:
        documentList: List with all documents in the collection of the database.
    """
    documentList = []
    client = MongoClient(address)
    client_db = client[database]
    client_db_collection = client_db[collection]
    document = client_db_collection.find()

    for item in document:
        documentList.append(item)
    return documentList


def getDocumentAtIndex(address, database, collection, index="0"):
    """
    Get a document from a collection at a specific index.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"].
        collection: String with the name of the collection. For example: "names" or "products".
        index: Function to use when parsing all documents. For example: "0", "10", "1000".

    Returns:
        document: The document found at the specified index.
    """
    return document


def searchDocuments(address, database, collection, searchterm, partialmatch=True, casesensitive=False, firstonly=True):
    """
    Search for documents where the name matches the search term.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"].
        collection: String with the name of the collection. For example: "names" or "products".
        searchterm: String with the term to search for. For example: "Andrelon", "Jack" or "February".
        partialmatch: Whether the search term has to be matched exactly or partially. True or False.
        casesensitive: Whether the search term will only match the exact case. True or False.
        firstonly: Whether the function will return only the first match. True or False.

    Returns:
        resultingDocuments: The resulting document(s).
    """
    return resultingDocuments


def parseDocuments(address, database, collection, function):
    """
    Parse all documents from a collection with a function.

    Args:
        database: String or list with database names. For example: "testdb" or ["testdb1", "testdb2", "testdb3"].
        collection: String with the name of the collection. For example: "names" or "products".
        function: Function to use when parsing all documents. For example: "mean", "min" or "max".

    Returns:
        result: The result of the function used.
    """
    return result


#databaseList = getDatabases(address)

#collectionDict = getCollections(databaseList)

#documentList = getCollectionDocuments("shopping", "products")
