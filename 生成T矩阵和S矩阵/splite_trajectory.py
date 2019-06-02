import datetime
import time
import pandas as pd

##按照时间将数据点划分成若干组轨迹序列，并且将他们编号，生成新的列tj_id

pathname = 'trajectory.csv'
data = pd.read_csv(pathname )

ccount = 0;
#源数据10分钟采集一次，以30分钟为分界线判断
step = 1800;
trjectory_num = []
pre = time.mktime(datetime.datetime.strptime(data['time'][0], '%Y-%m-%d %H:%M:%S').timetuple())

for d in data.values:
    now = time.mktime(datetime.datetime.strptime(d[4], '%Y-%m-%d %H:%M:%S').timetuple())
    if now-pre>=step:
        ccount += 1;
    trjectory_num.append(ccount)
    pre = now

data['tj_id'] = trjectory_num;
data.to_csv('trajectory.csv', index=False)
