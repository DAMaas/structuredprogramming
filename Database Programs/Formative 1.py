import MongoDB as mdb

address = "mongodb://localhost:27017/"

print(mdb.getCollections(mdb.getDatabases()))
