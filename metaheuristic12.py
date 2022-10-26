# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:56:08 2021

@author: subham
"""

import os 
import csv
import random

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the data from csv file
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

#Generating a random population of 0s and 1s whose length equals number of rows in csv file
def random_population(range_,cuckoo,row1):
    list=[]
    #random.seed(99)
    for i in range(range_):
        a=[]
        for j in range(1,row1):
            a.append(random.randint(0,1))
        list.append(a)
    return list

#Calculating fitness of each generated individual for selection
def fitness(range_,list,row1,cuckoo):
    fit=[]
    fitness_sum=0
    #print(len(list))
    for i in range(range_):
        for j in range(1,row1-1):
            if list[i][j]==1:
                fitness_sum=fitness_sum+(float(cuckoo[j][1])+float(cuckoo[j][2]))*(float(cuckoo[j][4]))
        fit.append(fitness_sum)
        fitness_sum=0
    return fit

#Selecting the individuals according to their fitness values 
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

#Conducting a single point crossover over the selected individuals such that among the 
#two individuals values are swapped over till the crossover point with a probability of 90%                   
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

#Conducting flip-bit mutation with a random probability of 10%
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

#Printing the scheduled job in a time optimized sequence
def job_schedule(x3,cuckoo):
    print()
    print("Order of job execution:")
    row=1
    row1=1
    for i in x3:
        for j in i:
            if j==1:
                print(cuckoo[row][0],"to resource number",cuckoo[row][3])
            row+=1
    for i in x3:
        for j in i:
            if j==0:
                print(cuckoo[row1][0],"to resource number",cuckoo[row1][3])
            row1+=1

#The functions written above are initiated in te main loop
def main_loop():
    range_=8
    gen=0
    gen_=100
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    #Calling the data from our required function 
    cuckoo,row1=load_data()
    list=random_population(range_,cuckoo,row1)
    #Iterating through several generations to find the best combination 
    while gen<gen_+1:
        print("Generation",gen)
        while True:
            #Passing the new generation to calculate its fitness,selection,reducing its range to
            #half as from each two individuals only one is passed to new generation
            fit=fitness(range_,list,row1,cuckoo)
            record1,list1=selection(range_,list,fit)
            range_=int(range_/2)
            
            #Operating with genetic operators after saving a copy of the previous generation
            #then using the cuckoo approach to replace the minimum in the individuals thus obtained
            #with the best in the previously copied version
            record1,list2=crossover(record1,row1)
            fit1=fitness(range_,list2,row1,cuckoo)
            fit2=fitness(range_,record1,row1,cuckoo)
            if max(fit1)>min(fit2):
                max_index_list2=fit1.index(max(fit1))
                min_index_record1=fit2.index(min(fit2))
                record1[min_index_record1]=list2[max_index_list2]
            
            #a similar approach is used in mutation as it changes the individuals randomly
            record1,list3=mutation(record1,row1)
            fit3=fitness(range_,list3,row1,cuckoo)
            fit4=fitness(range_,record1,row1,cuckoo)
            if max(fit3)>min(fit4):
                max_index_list3=fit3.index(max(fit3))
                min_index_record1=fit4.index(min(fit4))
                record1[min_index_record1]=list2[max_index_list3]
                
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
            
        #Updating the new generation with fresh values
        gen+=1
        range_=8
        x3.append(x2)
        list.clear()
        list=random_population(range_,cuckoo,row1)
        
    #Accumulating the best data available
    max_index=x1.index(max(x1))
    print()
    print("Solution found in generation:",max_index)
    print("Best sequence and fitness obtained are:")
    print(x3[max_index])
    print(max(x1))
    job_schedule(x3[max_index],cuckoo)

#To plot the chracteristics obtained fron the above computations
    sns.set_style("whitegrid")
    plt.plot(x1, color='tomato')
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Max fitness over generations")
    plt.show()

#The following lines make(s) the execution to start from the main loop         
if __name__=='__main__':
    main_loop()    