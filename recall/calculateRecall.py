import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def genX(data):
    user_num, grid_num, all_num = 100, 2500, 49961
    X = np.zeros((user_num, grid_num))
    for i, d in enumerate(data.values):
        X[d[4]][d[5]] += 1
    for i in range(user_num):
        X[i, :] = X[i, :] / sum(X[i, :])
    X = pd.DataFrame(X)
    X.columns = ['{}'.format(i) for i in range(1, grid_num + 1)]
    return X


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
            vec = vec[:: -1]
            for k in range(i * 10):
                topM += vec[k]
        res.append(topM)

    return res / total


def cal():
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


def drawGraph():
    Rs = np.array(pd.read_csv("recall_Xs.csv", header=None))
    Rt = np.array(pd.read_csv("recall_Xt.csv", header=None))
    real = calculate("x_train.csv")
    plt.figure(num=1)
    for i in range(1, 10):
        plt.plot(Rs[0] + 1, Rs[i], label="Xs_" + str(i))
    plt.legend()  # 显示图例
    plt.title("Recall_Xs")

    plt.figure(num=2)
    for i in range(1, 10):
        plt.plot(Rt[0] + 1, Rt[i], label="Xt_" + str(i))
    plt.legend()
    plt.title("Recall_Xt")

    plt.figure(num=3)
    for i in range(1, 4):
        plt.plot(Rs[0] + 1, Rs[i], label="Xs_" + str(i))
        plt.plot(Rt[0] + 1, Rt[i], label="Xt_" + str(i))
    plt.legend()
    plt.title("Xs-Xt")
    plt.show()  # 显示图片


def gen_train_eval(X, ratio):
    user_num, grid_num, all_num = 100, 2500, 49961
    x_train, x_eval = np.zeros((user_num, grid_num)), np.array(X)
    train_num, index, step, all_train_num = 0, 0, int((0.011 + ratio) * grid_num), int(ratio * all_num)
    while train_num < all_train_num:
        row, col = index // grid_num, index % grid_num
        if X.loc[row, '{}'.format(col + 1)] != 0 and x_train[row][col] == 0:
            x_train[row][col] = X.loc[row, '{}'.format(col + 1)]
            train_num += 1
        index = (step + index) % (grid_num * user_num)
    x_eval -= x_train
    x_train, x_eval = pd.DataFrame(x_train), pd.DataFrame(x_eval)
    x_train.columns, x_eval.columns = X.columns, X.columns
    return x_train, x_eval


if __name__ == '__main__':
    # data = pd.read_csv('user_query_data.csv')
    # X = genX(data)
    # x_train, x_eval = gen_train_eval(X=X, ratio=0.3)
    # pd.DataFrame(X).to_csv("X.csv", index=False)
    # pd.DataFrame(x_train).to_csv("x_train.csv", index=False)
    # pd.DataFrame(x_eval).to_csv("x_eval.csv", index=False)

    drawGraph()
