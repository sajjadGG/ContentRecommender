from pymongo import MongoClient


def get_db():
    with open('.config' , 'r') as f:
        l = f.readline()
        mongo_token = l.split(':=')[-1]
    client = MongoClient(mongo_token , serverSelectionTimeoutMS=360000)
    db = client['myFirstDatabase']
    return db