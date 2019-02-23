# Import dependencies


from VariableStore import tableFieldsProducts, keyListProducts, tableFieldsStock, keyListStock
import MongoDB as mdb
import PostgreSQL as pg
import DataFilter as df


# initialize PostgreSQL
pg.initDatabase("webshop")

# Get all documents from MongoDB collection
allDocuments = mdb.getAllDocuments(collection="products")

# Convert documents for PostgreSQL
convertedDocumentsProducts = df.convertDocuments(
    allDocuments, tableFieldsProducts, keyListProducts)

convertedDocumentsStock = df.convertDocuments(
    allDocuments, tableFieldsStock, keyListStock)

print(convertedDocumentsStock)

pg.insertDocuments(convertedDocumentsProducts, "webshop",
                   "products", tableFieldsProducts)
