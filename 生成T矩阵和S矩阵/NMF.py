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
#print (X[771])

#进行非负矩阵分解
model = NMF(n_components=20, alpha=0.01)
Vs = model.fit_transform(X)
MVsT = model.components_


print(Vs[771])
np.savetxt("Vs.csv",Vs,delimiter=",")
np.savetxt("MVsT.txt",MVsT,delimiter=",")