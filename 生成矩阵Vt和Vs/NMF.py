import numpy as np
from sklearn.decomposition import NMF

#读入矩阵S
f = open(r"S.txt")
line = f.readline()
data_list = []
while line:
    num = list(map(float,line.split(',')))
    data_list.append(num)
    line = f.readline()
f.close()
X = np.array(data_list)

#进行非负矩阵分解
model = NMF(n_components=20, alpha=0.01, l1_ratio=0)
Vt = model.fit_transform(X)
E = model.components_

np.savetxt("Vt.csv",Vt,fmt="%e",delimiter=",")
np.savetxt("E.csv",E,fmt="%e",delimiter=",")