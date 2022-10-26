# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:06:18 2021

@author: subham
"""

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

def csv_reader(filename):
    news=[]
    file=open(filename,encoding="utf8")
    for row in file:
        news.append(row)
    file.close()
    return news
    
def tokenize():
    news=csv_reader("data1.csv")
    tokenized_word=[]
    for i in range(len(news)):
        tokenized_word.append(word_tokenize(news[i]))
        
        
    fdist = FreqDist(tokenized_word)
    
    fdist.most_common(2) 
    fdist.plot(30,cumulative=False)
    plt.show()
    #tokenized_word=word_tokenize(text)
    #print(tokenized_word)
        
def main_loop():
    csv_reader("data1.csv")
    tokenize()
