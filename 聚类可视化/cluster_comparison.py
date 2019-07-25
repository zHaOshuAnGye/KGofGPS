#!/usr/bin/env python
# coding: utf-8

# In[38]:


import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler


# In[53]:


colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = np.hstack([colors] * 20)

clustering_names = ['Kmeans','MiniBatchKMeans', 'Ward',
    'AgglomerativeClustering', 'Birch']


# In[54]:


dataset = pd.read_csv('Vt.csv',header=None)


# In[55]:


from sklearn import metrics


# In[57]:


X= dataset
# normalize dataset for easier parameter selection
X = StandardScaler().fit_transform(X)
kmeans = cluster.KMeans(n_clusters=4)
two_means = cluster.MiniBatchKMeans(n_clusters=4)
ward = cluster.AgglomerativeClustering(n_clusters=4, linkage='ward',
                                       connectivity=connectivity)
spectral = cluster.SpectralClustering(n_clusters=4)



average_linkage = cluster.AgglomerativeClustering(
    linkage="average", affinity="cityblock", n_clusters=4,
    connectivity=connectivity)

birch = cluster.Birch(n_clusters=4)

clustering_algorithms = [kmeans,two_means, ward, spectral,average_linkage, birch]

for name, clf in zip(clustering_names, clustering_algorithms):
    pred = clf.fit_predict(X)
    print(name,metrics.calinski_harabaz_score(X,pred),metrics.silhouette_score(X,pred))

