from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
#TODO : read from conf
GLOVE_FILE = 'C:\\Dev\\RecommenderSystem\\w2v\\'
GLOVE_TYPE = 'glove.6B.100d'
glove_file = datapath('{}{}.txt'.format(GLOVE_FILE , GLOVE_TYPE))
word2vec_glove_file = get_tmpfile("{}.word2vec.txt".format(GLOVE_TYPE))
glove2word2vec(glove_file, word2vec_glove_file)
model = KeyedVectors.load_word2vec_format(word2vec_glove_file)
print(model.most_similar('obama'))

def collect_user_history():
    pass

def user_history_to_vector():
    pass

def find_most_similar_contents():
    pass

