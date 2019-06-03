import numpy as np

#读入矩阵T
f = open(r"T.txt")
line = f.readline()
data_list = []
while line:
    num = list(map(float,line.split(',')))
    data_list.append(num)
    line = f.readline()
f.close()
X = np.array(data_list)

#进行RSVD矩阵分解
feature=20
steps=200
gama=0.002
lamda=0.01
slowRate = 0.99
preRmse = 0.0000000000001
nowRmse = 0.0

Vs = np.zeros((X.shape[0], feature))
M=np.zeros((feature, feature))
temp = np.dot(M,Vs.T)

for step in range(steps):
    rmse = 0.0
    n = 0
    print("steps:")
    print(step)
    for u in range(X.shape[0]):
        for i in range(feature):
            if X[u, i] > 0 :
                pui = float(np.dot(Vs[u, :], temp[:, i]))
                eui = X[u, i] - pui
                rmse += pow(eui, 2)
                n += 1
                for k in range(feature):
                    # Rsvd的更新迭代公式
                    Vs[u, k] += gama * (eui * M[k, i] - lamda * Vs[u, k])
                    M[k, i] += gama * (eui * Vs[u, k] - lamda * M[k, i])
    # n次迭代平均误差程度
    nowRmse = np.sqrt(rmse * 1.0 / n)
    if (nowRmse > preRmse):
        pass
    else:
        break
    # 降低迭代的步长
    gama *= slowRate
    step += 1

np.savetxt("Vs.csv", Vs, fmt="%e",delimiter=",")
np.savetxt("M.csv",M, fmt="%e",delimiter=",")
