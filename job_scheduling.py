# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:57:34 2021

@author: subha
"""

import os 
import csv
import random

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

def random_population(range_,cuckoo,row1):
    list=[]
    #random.seed(99)
    for i in range(range_):
        a=[]
        for j in range(1,row1):
            a.append(random.randint(0,1))
        list.append(a)
    return list

def fitness(range_,list,row1,cuckoo):
    fit=[]
    fitness_sum=0
    #print(len(list))
    for i in range(range_):
        for j in range(1,row1-1):
            print(j)
            if list[i][j]==1:
                fitness_sum=fitness_sum+(float(cuckoo[j][1])+float(cuckoo[j][2]))*(float(cuckoo[j][4]))
        fit.append(fitness_sum)
        fitness_sum=0
    return fit

def selection(range_,list,fit):
    list1=list.copy()
    record=[]
    record1=[]
    for j in range(0,len(fit),2):
        if j+1<range_:
            if fit[j+1]>fit[j]:
                record.append(fit[j+1])
                record1.append(list[j+1])
            elif fit[j]==fit[j+1]:
                record.append(fit[j])
                record1.append(list[j])
            else:
                record.append(fit[j])
                record1.append(list[j])
    return record1,list1
                    
def crossover(record1,row1):
    list2=[]
    list2=record1.copy()
    temp=0
    cop=random.randint(0,500)
    for i in range(len(record1)):
        for j in range(1,row1-1):
            if random.random()<=0.9 and j<=cop and i+1<len(record1):
                temp=record1[i][j]
                record1[i][j]=record1[i+1][j]
                record1[i+1][j]=temp
    return record1,list2

def mutation(record1,row1):
    list3=[]
    list3=record1.copy()
    for i in range(len(record1)):
        for j in range(1,row1-1):
            if random.random()<=0.1:
                if record1[i][j]==1:
                    record1[i][j]=0
                else:
                    record1[i][j]=1
    return record1,list3

def main_loop():
    range_=8
    gen=0
    gen_=5
    x1=[]
    x2=[]
    x3=[]
    cuckoo,row1=load_data()
    while gen<gen_+1:
        
        list=random_population(range_,cuckoo,row1)
        if gen>0:
            list=random_population(range_-1,cuckoo,row1)
            list.append(x2)
        
        print("Generation",gen)
        while True:
            fit=fitness(range_,list,row1,cuckoo)
            record1,list1=selection(range_,list,fit)
            range_=int(range_/2)
        
            record1,list2=crossover(record1,row1)
            fit1=fitness(range_,list2,row1,cuckoo)
            fit2=fitness(range_,record1,row1,cuckoo)
            if max(fit1)>max(fit2):
                max_index_list2=fit1.index(max(fit1))
                max_index_record1=fit2.index(max(fit2))
                record1[max_index_record1]=list2[max_index_list2]
                
            record1,list3=mutation(record1,row1)
            fit3=fitness(range_,list3,row1,cuckoo)
            fit4=fitness(range_,record1,row1,cuckoo)
            if max(fit3)>max(fit4):
                max_index_list3=fit3.index(max(fit3))
                max_index_record1=fit4.index(max(fit4))
                record1[max_index_record1]=list2[max_index_list3]
                
            list=record1
            fit1=0
            fit2=0
            fit3=0
            fit4=0
            if len(record1)==1:
                x1.append(fitness(range_,record1,row1,cuckoo))
                x2=record1.copy()
                print(fitness(range_,record1,row1,cuckoo))
                break
        gen+=1
        range_=8
        x3.append(x2)
        list.clear()
        
    max_index=x1.index(max(x1))
    print()
    print("Solution found in generation:",max_index)
    print("Best sequence and fitness obtained are:")
    print(x3[max_index])
    print(max(x1))
        
if __name__=='__main__':
    main_loop()    