import MongoDB as mdb


# Import documents
firstDocument = mdb.getFirstDocument()
allDocuments = mdb.getAllDocuments()


# Get the first document and only output name and price
docName = mdb.filterOutputFields(firstDocument, "name")
docPrice = mdb.filterOutputFields(firstDocument, "price", "selling_price")
print("The first product, " + str(docName) +
      ", sells for " + str(docPrice / 100) + " euro.")


# Get the first document that starts with R
docWithR = mdb.filterFieldStartsWith(
    allDocuments, field="name", value="R", firstOnly=True)
print("First product that starts with R: " + str(docWithR))


# Get average price
averagePrice = mdb.filterAverage(allDocuments, "price", "selling_price")
print("The average price is " + str(averagePrice / 100) + " euro")
