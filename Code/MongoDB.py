# Import dependencies


from pymongo import MongoClient


# Initialize variables


address = "mongodb://localhost:27017/"
database = "shopping"
collection = "products"


# Define functions


def connectMongo(address="mongodb://localhost:27017/", database="shopping", collection="products"):
    clientbase = MongoClient(address)
    clientbase_db = clientbase[database]
    clientbase_db_collection = clientbase_db[collection]
    client = clientbase_db_collection
    return client


def getSingleDocument(search={}, filter=[]):
    """
    Get a single document from a collection. If no key and value is given it will return the first document.

    Args:
        key (optional): Dictionary key to search for. For example: "Name" or "Age".
        value (optional): Dictionary value to search for. For example: "Dion" or "22".
        returnkey (optional): Dictionary key to return; omits all other keys from the result. For example: "Name" or "Age".
        returnvalue (optional): Dictionary value to return; omits all other values from the result. For example: "Dion" or "22".

    Returns:
        document: The document that is found.
    """

    document = []
    client = connectMongo()

    if search != {}:
        document = client.find_one(search, projection=filter)
    else:
        document = client.find_one(search, projection=filter)
    return document


def getAllDocuments(search={}, filter=[]):
    """
    Get all documents from a collection. If no key and value is given it will return all documents.

    Args:
        key (optional): Dictionary key to search for. For example: "Name" or "Age".
        value (optional): Dictionary value to search for. For example: "Dion" or "22".
        returnkey (optional): Dictionary key to return; omits all other keys from the result. For example: "Name" or "Age".
        returnvalue (optional): Dictionary value to return; omits all other values from the result. For example: "Dion" or "22".

    Returns:
        document: The document that is found.
    """

    documentList = []
    client = connectMongo()

    document = client.find(search, projection=filter)
    for item in document:
        documentList.append(item)
    return documentList
