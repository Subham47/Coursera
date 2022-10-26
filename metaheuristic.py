# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:11:28 2021

@author: subham
"""

import os 
import csv
import random

range_=8
def load_data():
    cuckoo=[]
    row1=0
    if os.access("sajal1.csv",os.F_OK):
        file=open("sajal1.csv")
        for row in csv.reader(file):
            cuckoo.append(row)
            row1+=1
        file.close()
    return cuckoo,row1

def random_population():
    cuckoo,row1=load_data()
    list=[]
    random.seed(99)
    for i in range(range_):
        a=[]
        for j in range(1,row1):
            a.append(random.randint(0,1))
        list.append(a)
    return list

def fitness():
    cuckoo,row1=load_data()
    list=random_population()
    fit=[]
    fitness_sum=0
    for i in range(range_):
        for j in range(1,row1-1):
            if list[i][j]==1:
                fitness_sum=fitness_sum+(float(cuckoo[j][1])+float(cuckoo[j][2]))*float(cuckoo[j][4])
        fit.append(fitness_sum)
        fitness_sum=0
    return fit

def selection():
    cuckoo,row1=load_data()
    list=random_population()
    fit=fitness()
    list1=list.copy()
    #record=[]
    for j in range(len(fit),2):
        if fit[j]<fit[j+1] and j+1<=range_:
            print(j+1)
            fit[j]=fit[j+1]
        else:
            print(j+1)
            fit[j+1]=fit[j]
    return list,list1
                    
def crossover():
    cuckoo,row1=load_data()
    list,list1=selection()
    list2=[]
    list2=list.copy()
    temp=0
    cop=random.randint(0,500)
    for i in range(range_):
        for j in range(row1):
            if random.random()<=0.9 and j<=cop and i+1<len(list):
                temp=list[i][j]
                list[i][j]=list[i+1][j]
                list[i+1][j]=temp
    return list,list2

def mutation():
    cuckoo,row1=load_data()
    list,list2=crossover()
    list3=[]
    list3=list.copy()
    for i in range(range_):
        for j in range(1,row1-1):
            if random.random()<=0.1:
                if list[i][j]==1:
                    list[i][j]=0
                else:
                    list[i][j]=1
    return list,list3

def main_loop():
    load_data()
    random_population()
    fitness()
    selection()
    crossover()
    mutation()
    
if __name__=='__main__':
    main_loop()    