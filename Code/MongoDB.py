# Import dependencies


from pymongo import MongoClient
from ConfigParser import getConfig


# Define functions


def connectMongo(address="", database="", collection="", configFile="Code/Config.ini", configSection="MongoDBLogin"):
    """
    Connect to the Mongo daemon.

    Arguments:
        address:        Overrides config file if specified.
        database:       Overrides config file if specified.
        collection:     Overrides config file if specified.
        configFile:     Name and path of config file.
        configSection:  Name of the section in the config file.

    Returns:
        client:         The session that is made.
    """

    config = getConfig(configFile, configSection)
    if address == "":
        address = config["address"]
    if database == "":
        database = config["database"]
    if collection == "":
        collection = config["collection"]

    clientbase = MongoClient(address)
    clientbase_db = clientbase[database]
    clientbase_db_collection = clientbase_db[collection]
    client = clientbase_db_collection
    return client


def getFirstDocument(address="", database="", collection=""):
    """
    Get the first document.

    Arguments:
        None

    Returns:
        document: The document that is found.
    """

    document = []
    client = connectMongo(address, database, collection)

    document.append(client.find_one())

    return document


def getAllDocuments(address="", database="", collection=""):
    """
    Get all documents.

    Arguments:
        None

    Returns:
        documentList: The documents that are found.
    """

    documentList = []
    client = connectMongo(address, database, collection)

    documents = client.find()

    for item in documents:
        documentList.append(item)

    return documentList


def filterOutputFields(documents, field="", subfield="", outputString=False):
    """
    Filter: Only output a specific field or field and subfield.

    Arguments:
        documents:      List of documents to filter.
        field:          The field to include.
        value:          The subfield to include.
        outputString:   Output as a string. True or False.

    Returns:
        filter:         The result of the filter.
    """

    if outputString == True:
        filter = ""

        if subfield != "":
            if isinstance(documents, (list,)):
                for document in documents:
                    currentField = item[subfield]
                    filter = currentField
            else:
                currentField = documents[field][subfield]
                filter = currentField
        else:
            if isinstance(documents, (list,)):
                for document in documents:
                    currentField = document.get(field)
                    filter = currentField
                    break
            else:
                currentField = documents.get(field)
                filter = currentField
    else:
        filter = []
        if subfield != "":
            if isinstance(documents, (list,)):
                for document in documents:
                    currentField = document[field][subfield]
                    filter.append(currentField)
            else:
                currentField = documents[field][subfield]
                filter.append(currentField)
        else:
            if isinstance(documents, (list,)):
                for document in documents:
                    currentField = document.get(field)
                    filter.append(currentField)
            else:
                currentField = documents.get(field)
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
        filter:     The result of the filter.
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
        filter:     The result of the filter.
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
