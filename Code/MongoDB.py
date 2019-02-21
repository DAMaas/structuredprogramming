# Import dependencies


from pymongo import MongoClient


# Initialize variables


address = "mongodb://localhost:27017/"
database = "shopping"
collection = "products"


# Define functions


def connectMongo(address="mongodb://localhost:27017/", database="shopping", collection="products"):
    """
    Connect to the Mongo daemon.

    Arguments:
        address:    URL to connect to.
        databse:    The database to use.
        collection: The collection to use.

    Returns:
        document: The document that is found.
    """
    clientbase = MongoClient(address)
    clientbase_db = clientbase[database]
    clientbase_db_collection = clientbase_db[collection]
    client = clientbase_db_collection
    return client


def getFirstDocument():
    """
    Get the first document.

    Arguments:
        None

    Returns:
        document: The document that is found.
    """

    document = []
    client = connectMongo()

    document.append(client.find_one())

    return document


def getAllDocuments():
    """
    Get all documents.

    Arguments:
        None

    Returns:
        documentList: The documents that are found.
    """

    documentList = []
    client = connectMongo()

    documents = client.find()

    for item in documents:
        documentList.append(item)

    return documentList


def filterOutputFields(documents, field="", subfield="", firstOnly=True):
    """
    Filter: Only output a specific field or field and subfield.

    Arguments:
        documents:  List of documents to filter.
        field:      The field to include.
        value:      The subfield to include.
        firstOnly:  Only return the first document. True or False.

    Returns:
        filter: The result of the filter.
    """

    if firstOnly == True:
        filter = ""

        if subfield != "":
            for item in documents:
                currentField = item[field][subfield]
                filter = currentField
                break
        else:
            for item in documents:
                currentField = item[field]
                filter = currentField
                break
    else:
        filter = []
        if subfield != "":
            for item in documents:
                currentField = item[field][subfield]
                filter.append(currentField)

        else:
            for item in documents:
                currentField = item[field]
                filter.append(currentField)
    return filter


def filterFieldStartsWith(documents, field="", value="", firstOnly=True):
    """
    Filter: Find documents where a field starts with a letter.

    Arguments:
        documents:  List of documents to filter.
        field:      The field to check.
        value:      The value to check for.
        firstOnly:  Only return the first document. True or False.

    Returns:
        filter: The result of the filter.
    """

    filter = "No result found"

    if firstOnly == True:
        for item in documents:
            currentField = item[field]
            if currentField[0] == value:
                filter = currentField
                break
    else:
        filter = []
        for item in documents:
            currentField = item[field]
            if currentField[0] == value:
                filter.append(currentField)
    return filter


def filterAverage(documents, field="", subfield=""):
    """
    Filter: Get the average of a specific field in all documents.

    Arguments:
        documents:  List of documents to filter.
        field:      The field to check.
        subfield:   The subfield to check.

    Returns:
        filter: The result of the filter.
    """

    filter = 0
    totalValue = 0
    count = 0

    if subfield != "":
        for item in documents:
            currentField = item[field][subfield]
            totalValue += currentField
            count += 1

    else:
        for item in documents:
            currentField = item[field]
            totalValue += currentField
            count += 1

    filter = totalValue / count
    return filter
