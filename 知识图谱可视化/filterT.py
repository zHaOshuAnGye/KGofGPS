#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

t = np.array(pd.read_csv("T.csv", header=None))
print('begin')
counter=0
for i in range(2500):
    for j in range(i+1,2500):
        if t[i][j]>50 and i!=j:
            print('t1[',counter,']=',i,';','t2[',counter,']=',j,';')
            counter+=1
print('over,counter=',counter)