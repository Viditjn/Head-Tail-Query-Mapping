import gensim
import keras
import numpy as np
from keras.models import load_model
from mapper import *

Word2vec_PATH = './w2vNet.model'
modelNet = load_model('my_model2.h5')
modelVec = gensim.models.Word2Vec.load(Word2vec_PATH)
tailQueryList = []
with open('./tryQuery.txt') as f:
    for l in f:
        tailQueryList.append(l)
head_queries , head_X = createHeadVectors(modelVec)
head_queries = head_queries.reshape(head_queries.shape[0],-1)
for query in tailQueryList:
  print "================"
  print "Calculating for :", query
  tailVec =  wordTovec2(query,modelVec)
  l1 = len(head_queries)
  query_X = np.zeros((l1,word2vecLen),dtype=float)
  for i in range(len(head_queries)):
    query_X[i] = np.append(head_X[i],tailVec)
  queryAns = modelNet.predict(query_X)
  query_scorePair = np.concatenate((head_queries,queryAns),axis=1)
  # pdb.set_trace()
  query_scorePair = query_scorePair[np.argsort(query_scorePair[:, 1])]
  for i in range(5):
    print query," : ",query_scorePair[l1-i-1]
