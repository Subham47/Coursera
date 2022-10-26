# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:54:43 2021

@author: subha
"""

import os 
import csv
import random
import math

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

def cuckoo_levy(range_,row1,cuckoo,max_index_record1):
    gamma=random.random(0,1)
    beta=random.random(0,1)
    pi=3.143
    sigma_u=(gamma(1+beta)*math.sin(pi*beta))/(gamma*(1+beta/2)*beta*2**(beta-1)/2)**(1/beta)  
    sigma_v=1
    for i in range(range_):
        for j in range(1,row1-1):
            u=random.random()*sigma_u
            v=random.random()*sigma_v
            s=u/(abs(v)**(1/beta))
            x_new=int(cuckoo[i])+random.random()*0.01*s*(cuckoo[i]-cuckoo[max_index_record1])
                          
        
    
def random_population(range_,cuckoo,row1):
    list=[]
    random.seed(99)
    for i in range(range_):
        a=[]
        for j in range(1,row1):
            a.append(random.randint(0,1))
        list.append(a)
    return list

def fitness(range_,list,row1,cuckoo):
    fit=[]
    fitness_sum=0
    for i in range(range_):
        for j in range(1,row1-1):
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
    cop=random.randint(0,row1-1)
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
    cuckoo,row1=load_data()
    list=random_population(range_,cuckoo,row1)
    while True:
        fit=fitness(range_,list,row1,cuckoo)
        record1,list1=selection(range_,list,fit)
        range_=int(range_/2)
        
        record1,list2=crossover(record1,row1)
        fit1=fitness(range_,list2,row1,cuckoo)
        fit2=fitness(range_,record1,row1,cuckoo)
        if max(fit1)>min(fit2):
            max_index_list2=fit1.index(max(fit1))
            min_index_record1=fit2.index(min(fit2))
            record1[min_index_record1]=list2[max_index_list2]
            
        record1,list3=mutation(record1,row1)
        fit3=fitness(range_,list3,row1,cuckoo)
        fit4=fitness(range_,record1,row1,cuckoo)
        if max(fit3)>min(fit4):
            max_index_list3=fit3.index(max(fit3))
            min_index_record1=fit4.index(min(fit4))
            record1[min_index_record1]=list2[max_index_list3]
            
        list=record1
        
        if len(record1)==1:
            max_index_record1=fit4.index(max(fit4))
            cuckoo_levy(range_,row1,cuckoo,max_index_record1)
            break
        
        fit1=0
        fit2=0
        fit3=0
        fit4=0
    for i in record1:
        print(fitness(range_,record1,row1,cuckoo))
    
if __name__=='__main__':
    main_loop()    