import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df_features = pd.read_csv(r'data_using_method_in_paper/Vts _select.csv', encoding='gbk')  # 读入数据
'利用SSE选择k'
SSE = []  # 存放每次结果的误差平方和
for k in range(1, 15):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(df_features)
    SSE.append(estimator.inertia_)  # estimator.inertia_获取聚类准则的总和
X = range(1, 15)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, 'o-')
plt.show()