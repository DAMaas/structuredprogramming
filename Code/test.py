queryFields = "("

tableFields = ["id", "name", "brand", "gender", "price", "category",
               "subcategory", "subsubcategory", "outofstockdate", "recommendable", "fast_mover", "repeatpurchase"]

for item in tableFields:
    queryFields += item
    queryFields += ", "
queryFields = queryFields[:-2] + ")"
print(queryFields)
