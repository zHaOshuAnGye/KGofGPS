import csv
import string
import time
import math

#系数常量
a = 6378245.0
ee = 0.00669342162296594323
x_pi = 3.14159265358979324 * 3000.0 / 180.0;

#转换经度
def transformLat(lat,lon):
    ret = -100.0 + 2.0 * lat + 3.0 * lon + 0.2 * lon * lon + 0.1 * lat * lon +0.2 * math.sqrt(abs(lat))
    ret += (20.0 * math.sin(6.0 * lat * math.pi) + 20.0 * math.sin(2.0 * lat * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lon * math.pi) + 40.0 * math.sin(lon / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lon / 12.0 * math.pi) + 320 * math.sin(lon * math.pi  / 30.0)) * 2.0 / 3.0
    return ret

#转换纬度
def transformLon(lat,lon):
    ret = 300.0 + lat + 2.0 * lon + 0.1 * lat * lat + 0.1 * lat * lon + 0.1 * math.sqrt(abs(lat))
    ret += (20.0 * math.sin(6.0 * lat * math.pi) + 20.0 * math.sin(2.0 * lat * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * math.pi) + 40.0 * math.sin(lat / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lat / 12.0 * math.pi) + 300.0 * math.sin(lat / 30.0 * math.pi)) * 2.0 / 3.0
    return ret

#Wgs transform to gcj
def wgs2gcj(lat,lon):
    dLat = transformLat(lon - 105.0, lat - 35.0)
    dLon = transformLon(lon - 105.0, lat - 35.0)
    radLat = lat / 180.0 * math.pi
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    mgLat = lat + dLat
    mgLon = lon + dLon
    loc=[mgLat,mgLon]
    return loc

#gcj transform to bd2
def gcj2bd(lat,lon):
    x=lon
    y=lat
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    bd_lon = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    bdpoint = [bd_lon,bd_lat]
    return bdpoint

#wgs transform to bd
def wgs2bd(lat,lon):
    wgs_to_gcj = wgs2gcj(lat,lon)
    gcj_to_bd = gcj2bd(wgs_to_gcj[0], wgs_to_gcj[1])
    return gcj_to_bd;

if __name__ == '__main__':
    #(116.66,40.18)(116.16,39.68)
    lat1=40.18
    lon1=116.66
    lat2=39.68
    lon2=116.16
    print(wgs2bd(lat1,lon1))
    print(wgs2bd(lat2,lon2))

