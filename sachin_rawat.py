# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:00:53 2021

@author: subha
"""

import csv

def csv_reader(fileopen):
    #file=open(fileopen)
    for row in open(fileopen, "r"):
        yield row
    print(row)