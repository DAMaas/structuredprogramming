# Import dependencies

from VariableStore import tableProductsFields, keyListProducts
import MongoDB as mdb
import PostgreSQL as pg
import DataFilter as df


# Get all documents
allDocuments = mdb.getAllDocuments(collection="products")
singleDocument = mdb.getFirstDocument(collection="products")

# Filter documents

# pg.initDatabase("webshop")
df.makeDocumentsSQL(allDocuments, "products",
                    tableProductsFields, keyListProducts)
