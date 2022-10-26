# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:48:38 2021

@author: subha
"""

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
#from nltk.probability import FreqDist
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_multilabel_classification

def text_process(text):
    stemmer=WordNetLemmatizer()
    nopunc=[char for char in text if char not in string.punctuation]
    nopunc=''.join([i for i in nopunc if not i.isdigit()])
    nopunc=[word.lower() for word in nopunc.split() if word not in stopwords.words('english')]
    return [stemmer.lemmatize(word) for word in nopunc] 

def csv_reader(filename):
    news=[]
    file=open(filename,encoding="utf8")
    for row in file:
        news.append(row)
        #print(text_process(row))
    file.close()
    return news

def vectorization(list):
    dataset = pd.read_csv('data.csv')
    x = dataset.iloc[:, -1].values
    
    X_train, X_test = train_test_split(x, test_size=0.25, random_state=0)

    tfidfconvert=TfidfVectorizer(analyser=text_process,ngram_range=(1,3)).fit(X_train)
    print(len(tfidfconvert))
    X_transformed=tfidfconvert.transform(X_train)
    return X_transformed

def kmeancluster(X_transformed):
    modelkmeans=KMeans(n_clusters=3,init='k-means++',n_init=100)
    modelkmeans.fit(X_transformed)
    KMeans(algorithm='auto',copy_x=True,init='k-means++',max_iter=300,n_clusters=3,n_init=100,n_jobs=None,precompute_distances='auto',random_state=None,tol=0.0001,verbose=0)
       
def main():
    news=csv_reader("data.csv")
    #list=text_process()
    for element in news:
        list=text_process(element)
        X_transformed=vectorization(list)
        kmeancluster(X_transformed)   
    
if __name__=='__main__':
    main()
    
