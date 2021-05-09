from pymongo import MongoClient
from datetime import datetime , timedelta
with open('.config' , 'r') as f:
    l = f.readline()
    mongo_token = l.split(':=')[-1]

# print(mongo_token)
client = MongoClient(mongo_token , serverSelectionTimeoutMS=360000)
db = client['myFirstDatabase']
print(db.list_collection_names())

c = db.userhistories.aggregate([
        {
            '$match' : {
                'createdAt' : {
                    '$gt' : datetime.now() - timedelta(days=3)
                }
            }
        },
        {
            '$lookup' : {
                'from' : 'users',
                'localField' : 'user',
                'foreignField' : '_id',
                'as' : 'userdata'
            }
        },
        {
        "$unwind": "$userdata"
        },
        {
            '$lookup' : {
                'from' : 'contents',
                'localField' : 'content',
                'foreignField' : '_id',
                'as' : 'contentdata'
            }
        },
        {
        "$unwind": "$contentdata"
        },
        {
            '$group':{
                '_id': {'user' : '$userdata.username'},
                'contents' : {'$addToSet' : '$contentdata.des'}
            }
        }
    ])    