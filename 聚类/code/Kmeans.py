#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

#参数初始化

inputfile = 'data_using_method_in_paper/Vts_select.csv' #销量及其他属性数据
# names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         # 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         # 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD',
         # 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN',
         # 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX'
         # ]
names = ['A', 'B', 'C']
outputfile = 'data_using_method_in_paper/outputVts_select4_detail.csv' #保存结果的文件名
out = 'data_using_method_in_paper/outputVts_select4_basic.csv' #保存结果的文件名

k = 4 #聚类的类别

iteration = 1000 #聚类最大循环次数

data = pd.read_csv(inputfile,names=names) #读取数据

# data_zs = 1.0*(data - data.mean())/data.std() #数据标准化

# print(np.isnan(data).any())

model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类, 并发数4

model.fit(data) #开始聚类

#简单打印结果

r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目

r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心

r = pd.concat([r2, r1], axis = 1) #横向连接(0是纵向), 得到聚类中心对应的类别下的数目

r.columns = list(data.columns) + [u'类别数目'] #重命名表头

print(r)
r.to_csv(out)

#详细输出原始数据及其类别

r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细

#输出每个样本对应的类别

r.columns = list(data.columns) + [u'聚类类别'] #重命名表头

r.to_csv(outputfile) #保存结果

tsne = TSNE()
tsne.fit_transform(data) #进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index = data.index) #转换数据格式
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'g.')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
d = tsne[r[u'聚类类别'] == 3]
plt.plot(d[0], d[1], 'y.')
# d = tsne[r[u'聚类类别'] == 4]
# plt.plot(d[0], d[1], 'k.')
# d = tsne[r[u'聚类类别'] == 5]
# plt.plot(d[0], d[1], 'c.')
# d = tsne[r[u'聚类类别'] == 6]
# plt.plot(d[0], d[1], 'm.')
# d = tsne[r[u'聚类类别'] == 7]
# plt.plot(d[0], d[1], color='#FF69B4', linestyle=':', marker='.')
plt.show()
