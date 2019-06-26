import numpy as np
import pandas as pd


def calculate(fileName):
    res = []
    X = np.array(pd.read_csv(fileName))
    total = 0
    for i in range(100):
        for j in range(2500):
            total += X[i][j]

    for i in range(1, 11):
        topM = 0
        for j in range(100):
            vec = X[j]
            vec = np.sort(vec)
            vec = vec[: : -1]
            for k in range(i*10):
                topM += vec[k]
        res.append(topM)

    return res/total


if __name__ == '__main__':
    recall = []
    for i in range(1, 101):
        print(i)
        recall.append(calculate("absX/Xt_" + str(i) + ".csv"))
    pd.DataFrame(recall).to_csv("recall_Xt.csv", index=False)

    recall = []
    for i in range(1, 101):
        print(i)
        recall.append(calculate("absX/Xs_" + str(i) + ".csv"))
    pd.DataFrame(recall).to_csv("recall_Xs.csv", index=False)