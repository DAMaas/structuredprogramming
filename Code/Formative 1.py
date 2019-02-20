import MongoDB as mdb


firstdoc = mdb.getSingleDocument(filter={"_id": False, "name": True})
startwithR = mdb.getSingleDocument({'name': {'$regex': '^R'}}, filter={
                                   "_id": False, "name": True})
priceList = mdb.getAllDocuments(
    filter={"_id": False, "price.selling_price": True})

total = 0
count = 0

for item in priceList:
    total += item["price"]["selling_price"]
    count += 1

average = total / count / 100

print("Eerste product in de database: " + str(firstdoc))
print("Eerste product dat begint met R: " + str(startwithR))
print("De gemiddelde prijs is " + str(average) + " euro")
