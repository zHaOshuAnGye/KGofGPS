import numpy as np
import pandas as pd


def main():
    U = np.array(pd.read_csv("U.csv"))
    V = np.array(pd.read_csv("V.csv"))
    Vt = np.array(pd.read_csv("Vt.csv", header=None))
    Vs = np.array(pd.read_csv("Vs.csv", header=None))
    iteration = 100
    for sigma in range(iteration):
        print(sigma)
        X = np.zeros((100, 2500))
        for i in range(100):
            for j in range(2500):
                X[i][j] = np.random.normal(loc=np.dot(U[i], V[j]+Vt[j]), scale=(sigma+1)/iteration)
        pd.DataFrame(X).to_csv("X/Xt_"+str(sigma+1)+".csv", index=False)

    for sigma in range(iteration):
        print(sigma)
        X = np.zeros((100, 2500))
        for i in range(100):
            for j in range(2500):
                X[i][j] = np.random.normal(loc=np.dot(U[i], V[j]+Vs[j]), scale=(sigma+1)/iteration)
        pd.DataFrame(X).to_csv("X/Xs_"+str(sigma+1)+".csv", index=False)


if __name__ == '__main__':
    main()