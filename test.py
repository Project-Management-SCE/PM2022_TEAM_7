import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:medical7@cluster0.g6nvd.mongodb.net/project?retryWrites=true&w=majority")
db = client["project"]
collection=db["drugs_drugs"]

mylist = [
  {"title": "gdfag", "price": "dd", "category": "S", "label": "P"}
]

x=collection.insert_many(mylist)


