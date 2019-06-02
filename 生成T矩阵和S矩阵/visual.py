#星期转化时间为24*2和24*7
#周六 0
#周日 1
#周一 2

#展示7*24个数据频次分布
import pandas as pd
import os
from matplotlib import pyplot

#绘制柱状图
def drawBar(grades):

    pyplot.hist(grades,range(47))
    pyplot.xticks(range(0,47,5))

    #设置横坐标的文字说明
    pyplot.xlabel('Hours')
    #设置纵坐标的文字说明
    pyplot.ylabel('Frequency')
    #设置标题
    pyplot.title('Frequency of Hours')
    #绘图
    pyplot.show()

time = []

pathname = 'trajectory.csv'

data = pd.read_csv(pathname)
#存在空数据


for d in data.values:
    if(int(d[7])<48):
        time.append(d[7])

print (time)
drawBar(time)