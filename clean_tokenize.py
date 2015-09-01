# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 03:52:36 2015

@author: happywwy1991
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None
    
wordnet_lemmatizer = WordNetLemmatizer()

f = open('./data/all_review', 'r').read().splitlines()
clean_text = open('./data/input_review', 'w')

all_token = []

for line in f:
    if '##' in line:
        partition = line.split('##')
        tokens = word_tokenize(partition[1])
        pos_review = nltk.pos_tag(tokens)
        
        word_pos = {}
        for item in pos_review:
            word_pos[item[0]] = penn_to_wn(item[1])
        
        for token in tokens:
            if token in word_pos.keys():
                if word_pos[token] != None:
                    token = wordnet_lemmatizer.lemmatize(token, word_pos[token])
            
            token = token.lower()
            
            all_token.append(token)
            
for term in all_token:   
    clean_text.write(term + ' ')
        #sentences.write('\n')
    
clean_text.close()