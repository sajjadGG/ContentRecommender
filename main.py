from pymongo import MongoClient

with open('.config' , 'r') as f:
    l = f.readline()
    mongo_token = l.split(':=')[-1]

# print(mongo_token)
client = MongoClient(mongo_token , serverSelectionTimeoutMS=360000)
db = client['myFirstDatabase']
print(db.list_collection_names())