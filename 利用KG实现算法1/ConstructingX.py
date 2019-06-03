import pandas as pd
import numpy as np

user_num, grid_num, all_num = 100, 2500, 49961##49961为X中值不为零的记录的个数
data = pd.read_csv('../data/user_query_data.csv')#用户数据文件路径


def gen_X(data): ##生成X  Xi,j表示用户i到网格编号j的地点的频率
    X = np.zeros((user_num, grid_num))
    for i, d in enumerate(data.values):
        X[d[4]][d[5]] += 1
    for i in range(user_num):
        X[i,:] = X[i,:]/sum(X[i,:])
    X = pd.DataFrame(X)
    X.columns = ['{}'.format(i) for i in range(1, grid_num+1)]
    return X


def gen_train_eval(X, ratio): ##划分训练集和验证集：ratio为训练集中非零值占总的X非零值个数的比例
    x_train, x_eval = np.zeros((user_num, grid_num)), np.array(X)
    train_num, index, step, all_train_num = 0, 0, int((0.011+ratio)*grid_num), int(ratio*all_num)
    while train_num<all_train_num:
        row, col = index//grid_num, index%grid_num
        if X.loc[row, '{}'.format(col+1)]!=0 and x_train[row][col]==0:
            x_train[row][col] = X.loc[row, '{}'.format(col+1)]
            train_num += 1
        index = (step+index)%(grid_num*user_num)
    x_eval -= x_train
    x_train, x_eval = pd.DataFrame(x_train), pd.DataFrame(x_eval)
    x_train.columns, x_eval.columns = X.columns, X.columns
    return x_train, x_eval

def latent_factor_model(data, k, iteration):## k为隐变量数
    data = np.array(data)
    U, V = np.random.rand(user_num, k), np.random.rand(grid_num, k)
    learning_rate, lambda_ = 0.01, 0.01
    for t in range(iteration):
        loss = 0
        for i in range(user_num):
            for j in range(grid_num):
                if abs(data[i][j])>1e-4:
                    error = data[i][j] - np.dot(U[i], V[j])
                    loss += abs(error)
                    for r in range(k):
                        gradient_u = error*V[j][r] - lambda_ *U[i][r]
                        gradient_v = error*U[i][r] - lambda_ *V[i][r]
                        U[i][r] += learning_rate*gradient_u
                        V[j][r] += learning_rate*gradient_v
        print("iteration:{}\tloss:{}".format(t, round(loss,4)))
    return U,V

X = gen_X(data)
# value_true = []
# for i in range(100):
#     for j in range(1, 2501):
#         if X.loc[i, '{}'.format(j)]!=0:
#             value_true.append(X.loc[i, '{}'.format(j)])
x_train, x_eval = gen_train_eval(X=X, ratio=0.3)
U, V = latent_factor_model(data=x_train, k=20, iteration=300)
U, V = pd.DataFrame(U), pd.DataFrame(V)
U.to_csv('U.csv', index=False)
V.to_csv('V.csv', index=False)
