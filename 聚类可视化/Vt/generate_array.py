#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

data = pd.read_csv('res.csv',header=None)
data


# In[14]:


ccount1 = 0
ccount2 = 0
ccount3 = 0
ccount4 = 0
for d in data.values:
    if d[1] == 0:
        print("t1[{0}] = {1}".format(ccount1,d[0]))
        ccount1 += 1
    if d[1] == 1:
        print("t2[{0}] = {1}".format(ccount2,d[0]))
        ccount2 += 1
    if d[1] == 2:
        print("t3[{0}] = {1}".format(ccount3,d[0]))
        ccount3 += 1
    if d[1] == 3:
        print("t4[{0}] = {1}".format(ccount4,d[0]))
        ccount4 += 1
print("ccount1={0}".format(ccount1))
print("ccount2={0}".format(ccount2))
print("ccount3={0}".format(ccount3))
print("ccount4={0}".format(ccount4))

