from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
#TODO : read from conf
GLOVE_FILE = 'C:\\Dev\\RecommenderSystem\\w2v\\'

glove_file = datapath('{}glove.6B.100d.txt'.format(GLOVE_FILE))
word2vec_glove_file = get_tmpfile("glove.6B.100d.word2vec.txt")
glove2word2vec(glove_file, word2vec_glove_file)
model = KeyedVectors.load_word2vec_format(word2vec_glove_file)
print(model.most_similar('obama'))