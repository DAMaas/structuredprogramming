# PostgresSQL.py
tableDict = {"webshop": (
    """
    CREATE TABLE products (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(255),
    gender VARCHAR(255),
    price INT,
    category VARCHAR(255),
    subcategory VARCHAR(255),
    subsubcategory VARCHAR(255),
    outofstockdate DATE,
    recommendable BOOLEAN,
    fast_mover BOOLEAN,
    repeatpurchase BOOLEAN
    );
    """,
    """
    CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    productid INT NOT NULL REFERENCES products (id),
    date VARCHAR(255),
    stocklevel INT
    );
    """
)}


# Summative 1.py
tableFieldsProducts = ["id", "name", "brand", "gender", "price", "category",
                       "subcategory", "subsubcategory", "outofstockdate", "recommendable", "fast_mover", "repeatpurchase"]

keyListProducts = ["_id", "name", "brand", "gender", ["price", "selling_price"], "category", "sub_category",
                   "sub_sub_category", "predict_out_of_stock_date", "recommendable", "fast_mover", "herhaalaankopen"]


tableFieldsStock = ["id", "productid", "date", "stocklevel"]

keyListStock = ["id", "productid", ["stock", "date"], ["stock", "stock_level"]]
