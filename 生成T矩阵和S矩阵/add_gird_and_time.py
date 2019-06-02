#对于经纬度划分区域块编号
#根据星期转化时间为24*2和24*7
#周六 0
#周日 1
#周一 2
import pandas as pd
import time,datetime
import  os
for i in range(1,201):
    name  = str(i)+'.txt'
    pathname = 'E:\\T-driveTaxi\\'

    #存在空数据
    if os.path.getsize(pathname + name)==0:
        continue

    data = pd.read_csv(pathname + name,header=None)

    #对于网格区域进行划分
    grid_num = []
    max_longitude, min_longitude, max_latitude, min_latitude = 116.66, 116.16, 40.18, 39.68
    for d in data.values:
        longitude, latitude = d[2], d[3]#将当前记录的经纬度赋值给longitude，latitude
        if longitude>=max_longitude or longitude<min_longitude or latitude>=max_latitude or latitude<min_latitude:
            grid_num.append(-1)
        else:
            grid_num.append(int((latitude-min_latitude)*100)*50+ int((longitude-min_longitude)*100))
    #print (grid_num)
    string = str(4)
    #print (len(grid_num))
    #print (data.shape[0])
    data[str(string)] = grid_num[:len(grid_num)]
    #pd.concat([data,pd.DataFrame(columns=grid_num[:len(grid_num)])])
    #pd.concat([data, pd.DataFrame(columns=grid_num[:len(grid_num) - 1:-1])])

    #对于时间进行划分
    time = []
    for d in data.values:
        daytime = (d[1])
        code = (int(datetime.datetime.strptime(daytime, '%Y-%m-%d %H:%M:%S').strftime("%w"))+2)%7
        print(code)
        time.append(code*24+int(d[1].split(' ')[1].split(':')[0]))
        #time.append(d[1].split(' ')[1].split(':')[0])
    #print (time)
    data['5'] = time
    data.to_csv('E:\\T-driveTaxi\\gird_time_'+name, index=False)

