# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:04:43 2015

@author: wangwenya
"""
from gensim.models.word2vec import Word2Vec
from sklearn.cluster import KMeans

model = Word2Vec.load('yelp_review.model')
word_vectors = model.syn0

num_clusters = 300
kmeans_clustering = KMeans( n_clusters = num_clusters )

idx = kmeans_clustering.fit_predict( word_vectors )

word_centroid_map = dict(zip( model.index2word, idx ))

'''
def create_bag_of_centroids(wordlist, word_centroid_map):
    
    num_centroids = max( word_centroid_map.values() ) + 1
    bag_of_centroids = np.zeros( num_centroids, dtype="float32" )
    
    for word in wordlist:
        if word in word_centroid_map:
            index = word_centroid_map[word]
            bag_of_centroids[index] += 1
'''

word_cluster = open('word_cluster.txt', 'w')

for i in model.index2word:
    
    word = str(i)
    word_cluster.write(word + ' ' + str(word_centroid_map[word]))
    word_cluster.write('\n')
    
word_cluster.close()