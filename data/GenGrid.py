import pandas as pd

max_id = 2000##需要多少辆车的数据，修改这里就可以

max_longitude, min_longitude, max_latitude, min_latitude = 116.66, 116.16, 40.18, 39.68

def get_grid_num(data):
    datas = []
    for i,d in enumerate(data.values):
        d = d.tolist()
        longitude, latitude = d[2], d[3]#将当前记录的经纬度赋值给longitude，latitude
        if longitude>=max_longitude or longitude<min_longitude or latitude>=max_latitude or latitude<min_latitude:
            d.append(-1)
        else:
            d.append(int((latitude-min_latitude)*100)*50+ int((longitude-min_longitude)*100))
        datas.append(d)
    datas = pd.DataFrame(datas)
    datas.columns = ['id', 'time', 'longitude', 'latitude', 'grid_num']
    datas = datas[datas['grid_num']!=-1]
    return datas

def get_date_features(data):
    data['time'] = pd.to_datetime(data['time'])
    data['weekday'] = data['time'].dt.dayofweek
    data['weekday'] = (data['weekday'] + 2)%7
    data['hour'] = data['time'].dt.hour
    data['hour_in_week'] = data['weekday']*24 + data['hour']
    return data

all_data = pd.read_csv('release/taxi_log_2008_by_id/1.txt')
all_data = get_grid_num(all_data)

for i in range(2, max_id):
    if i%50==0:
        print(i)
    try:
        data = pd.read_csv('release/taxi_log_2008_by_id/{}.txt'.format(i))##
        data = get_grid_num(data)
        all_data = pd.concat([all_data, data], axis=0, sort=True)
    except:
        pass
all_data = get_date_features(all_data)
all_data.to_csv('trajectory.csv', index=False)
