# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:31:14 2021

@author: subha
"""
#x1 in range 0 to 1(arrival time)
#x2 in range 0 to 400(burst time)

def cuckoo_levy_initial(cuckoo):
    list=[]
    gamma=random.random(0,1)
    beta=random.random(0,1)
    pi=3.143
    sigma_u=(gamma(1+beta)*math.sin(pi*beta))/(gamma*(1+beta/2)*beta*2**(beta-1)/2)**(1/beta)  
    sigma_v=1
    for i in range(range_):
        for j in range(1,row1-1)    
            u=random.random()*sigma_u
            v=random.random()*sigma_v
            s=u/(abs(v)**(1/beta))
            max1=0
            max2=0
            x
            for x1 in range(1,row1-1):
                if(max1<cuckoo[x][1]):
                    max1=cuckoo[x][1]
                if(max2<cuckoo[x][2])
                    max2=cuckoo[x][2]
            x1_new=cuckoo[j][1]+random.random()*0.01*s*(cuckoo[j][1]-max1)
            x2_new=cuckoo[j][2]+random.random()*0.01*s*(cuckoo[j][2]-max2)
            