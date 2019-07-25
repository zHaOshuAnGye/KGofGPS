#!/usr/bin/env python
# coding: utf-8

# In[90]:


from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from scipy.cluster.vq import vq,kmeans,whiten
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Vt.csv',header=None)


# In[91]:


len(data.values)
data.values


# In[92]:


X = data.values
X


# In[94]:


estimator = KMeans(n_clusters=4)#造聚类器
estimator.fit(X)#聚类
l = pd.DataFrame(estimator.labels_)
l[0].value_counts()


# In[95]:


from sklearn.cluster import KMeans,AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import MeanShift
from sklearn.metrics import homogeneity_completeness_v_measure
from sklearn import mixture
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster


# In[98]:



estimator = AgglomerativeClustering(n_clusters=4)#造聚类器
estimator.fit(X)#聚类
l = pd.DataFrame(estimator.labels_)
l.to_csv('res.txt',header=None,index=True)
#l.to_csv('res_sk.txt',header=None,index=False)


# In[99]:


data = pd.read_csv('res.txt',header=None)
data


# In[100]:


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





