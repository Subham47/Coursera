# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:52:10 2021

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
#from sklearn.datasets import make_multilabel_classification

def text_process(text):
    stemmer=WordNetLemmatizer()
    nopunc=[char for char in text if char not in string.punctuation]
    nopunc=''.join([i for i in nopunc if not i.isdigit()])
    nopunc=[word.lower() for word in nopunc.split() if word not in stopwords.words('english')]
    return [stemmer.lemmatize(word) for word in nopunc] 


def main():
    dataset = pd.read_csv('data.csv')
    text_process(dataset)
    x = dataset.iloc[:, -1].values
    
    X_train, X_test = train_test_split(x, test_size=0.25, random_state=0)

    tfidfconvert=TfidfVectorizer(analyzer=text_process).fit(X_train)
    print(len(tfidfconvert))
    X_transformed=tfidfconvert.transform(X_train)
    
    modelkmeans=KMeans(n_clusters=3,init='k-means++',n_init=100)
    modelkmeans.fit(X_transformed)
    KMeans(algorithm='auto',copy_x=True,init='k-means++',max_iter=300,n_clusters=3,n_init=100,n_jobs=None,precompute_distances='auto',random_state=None,tol=0.0001,verbose=0)
    
if __name__=='__main__':
    main()
    
    