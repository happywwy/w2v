# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:49:39 2015

@author: macbook
"""

# import modules and set up logging
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

train = True
output  = True

vecSize = 100

if train:
    # load up unzipped corpus from http://mattmahoney.net/dc/text8.zip
    sentences = word2vec.Text8Corpus('./data/yelp_review')
    # train the skip-gram model; default window=5
    model = word2vec.Word2Vec(sentences, size=vecSize, min_count = 3, iter = 10)
    # ... and some hours later... just as advertised...200
    # pickle the entire model to disk, so we can load&resume training later
    model.save('./data/yelp_review.model')


if output:
    f = open('./data/w2v_yelp_review.txt', 'w')
    for i in model.index2word:
        #print i
        word = str(i)
        f.write(word+",")
        #f.write(word +","+str(model[i])+","+"\n")
        for j in range(vecSize):
            wordvector = str(model[i][j])+","
            f.write(wordvector)
        f.write("\n")
            
    f.close()
   