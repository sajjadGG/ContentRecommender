from pymongo import MongoClient
from datetime import datetime , timedelta
from contentBased import *
with open('.config' , 'r') as f:
    l = f.readline()
    mongo_token = l.split(':=')[-1]

# print(mongo_token)
client = MongoClient(mongo_token , serverSelectionTimeoutMS=360000)
db = client['myFirstDatabase']
print(db.list_collection_names())

c = list(collect_user_history(db))
print(len(c))
uw = user_history_to_vector(c)
suggests = find_most_similar_contents(list(db.contents.find()) , uw)

