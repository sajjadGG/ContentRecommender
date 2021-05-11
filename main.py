from pymongo import MongoClient
from datetime import datetime , timedelta
import requests
from contentBased import *

API_ENDPOINT  = 'https://sharpsback.herokuapp.com/content/suggestions' 
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
#TODO : send in batches
res = requests.put(API_ENDPOINT , json = {'suggesters' : suggests})