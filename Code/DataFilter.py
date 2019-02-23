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
                    field = item[0]
                    subfield = item[1]
                    dictKey = str(field) + "." + str(subfield)
                    filteredDict[dictKey] = mdb.filterOutputFields(
                        document, field=field, subfield=subfield, outputString=True)
                else:
                    filteredDict[item] = mdb.filterOutputFields(
                        document, field=item, outputString=True)
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


def makeDocumentsSQL(allDocuments, table, tableFields, keyList):
    # Create query parts
    queryFields = "("
    for item in tableFields:
        queryFields += item
        queryFields += ", "
    queryFields = queryFields[:-2] + ")"
    print(queryFields)

    matchToList = tableFields
    matchFromList = keyList

    # Make a filtered dictionary per document
    for document in allDocuments:
        print("Processing document " +
              str(allDocuments.index(document) + 1) + " of " + str(len(allDocuments)) + "...")
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

        cleanDict = filteredDict
        print(cleanDict)

        #cur.execute("""INSERT INTO some_table (an_int, a_date, another_date, a_string) VALUES (%(int)s, %(date)s, %(date)s, %(str)s);""", {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)})
