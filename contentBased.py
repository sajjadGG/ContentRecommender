from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from datetime import datetime , timedelta
from DB import get_db
#TODO : read from conf
GLOVE_FILE = 'C:\\Dev\\RecommenderSystem\\w2v\\'
GLOVE_TYPE = 'glove.6B.100d'
glove_file = datapath('{}{}.txt'.format(GLOVE_FILE , GLOVE_TYPE))
word2vec_glove_file = get_tmpfile("{}.word2vec.txt".format(GLOVE_TYPE))
glove2word2vec(glove_file, word2vec_glove_file)
model = KeyedVectors.load_word2vec_format(word2vec_glove_file)
print(model.most_similar('obama'))

def collect_user_history():
    db = get_db()
    #TODO : make query more efficient
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
    return c

def user_history_to_vector(c , model = model):
    u = {}
    for k in c:
        user = k['_id']['user']
        contents = l['contents']
        #TODO : preprocess contents 
        return sum([model.get_vector(w) for s in contents for w in s.split() if w in model])
        

def find_most_similar_contents():
    pass

