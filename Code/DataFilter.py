# Import dependencies


import MongoDB as mdb
import PostgreSQL as pg


# Define functions


def outputInterestingData(documents, keyList):
    filteredDict = {}
    processTheseDocuments = documents

    if isinstance(processTheseDocuments, (list,)):
        for document in processTheseDocuments:
            for item in keyList:
                if isinstance(item, list):
                    if isinstance(document[item[0]][item[1]], list):
                        print("HOLLER")
                    else:
                        field = item[0]
                        subfield = item[1]
                        dictKey = str(field) + "." + str(subfield)
                        filteredDict[dictKey] = mdb.filterOutputFields(
                            processTheseDocuments, field=field, subfield=subfield, outputString=True)
                else:
                    filteredDict[item] = mdb.filterOutputFields(
                        processTheseDocuments, field=item, outputString=True)
    else:
        for item in keyList:
            if isinstance(item, list):
                field = item[0]
                subfield = item[1]
                dictKey = str(field) + "." + str(subfield)
                filteredDict[dictKey] = mdb.filterOutputFields(
                    processTheseDocuments, field=field, subfield=subfield, outputString=True)
            else:
                filteredDict[item] = mdb.filterOutputFields(
                    processTheseDocuments, field=item, outputString=True)
    return filteredDict


def convertDocuments(allDocuments, tableFields, keyList):
    convertedDocuments = []

    matchToList = tableFields
    matchFromList = keyList

    # Make a filtered dictionary per document
    for document in allDocuments:
        print("Converting document "
              + str(allDocuments.index(document) + 1) + " of " + str(len(allDocuments)) + "...")

        filteredDict = outputInterestingData(document, keyList)

        # Massage the filtered dictionary to the right values for SQL
        for item in matchToList:
            if isinstance(matchFromList[matchToList.index(item)], (list,)):
                currentItem = matchFromList[matchToList.index(item)]
                fieldString = ""
                for itemInList in currentItem:
                    fieldString += itemInList
                    fieldString += "."
                fieldString = fieldString[:-1]
                filteredDict[item] = filteredDict.pop(fieldString)
            else:
                filteredDict[item] = filteredDict.pop(
                    matchFromList[matchToList.index(item)])

        convertedDocuments.append(filteredDict)

    print(str(len(allDocuments)) + " documents converted succesfully\n")

    return convertedDocuments


# def convertNestedDocuments(allDocuments, tableFields, keyList):
#     convertedDocuments = []
#
#     matchToList = tableFields
#     matchFromList = keyList
#
#     # Make a filtered dictionary per document
#     for document in allDocuments:
#         print("Converting document "
#               + str(allDocuments.index(document) + 1) + " of " + str(len(allDocuments)) + "...")
#
#         for item in keyList
#         filteredDict = outputInterestingData(document, keyList)
#
#         # Massage the filtered dictionary to the right values for SQL
#         for item in matchToList:
#             if isinstance(matchFromList[matchToList.index(item)], (list,)):
#                 currentItem = matchFromList[matchToList.index(item)]
#                 fieldString = ""
#                 for itemInList in currentItem:
#                     fieldString += itemInList
#                     fieldString += "."
#                 fieldString = fieldString[:-1]
#                 filteredDict[item] = filteredDict.pop(fieldString)
#             else:
#                 filteredDict[item] = filteredDict.pop(
#                     matchFromList[matchToList.index(item)])
#
#         convertedDocuments.append(filteredDict)
#
#     print(str(len(allDocuments)) + " documents converted succesfully\n")
#
#     return convertedDocuments


def makeSQLQuery(table, tableFields):
    queryFunction = "INSERT INTO "
    queryDefinition = "VALUES "
    queryTable = table

    queryFields = " ("
    queryValues = "("

    for item in tableFields:
        queryFields += item
        queryFields += ", "
        queryValues += "%("
        queryValues += item
        queryValues += ")s, "

    queryFields = queryFields[:-2] + ") "
    queryValues = queryValues[:-2] + ");"

    query = queryFunction + queryTable + \
        queryFields + queryDefinition + queryValues

    return query
