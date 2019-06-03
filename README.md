# KGofGPS
​	复现论文**UnderstandingPeopleLifestyles: ConstructionofUrbanMovementKnowledge GraphfromGPSTrajectory**的内容。

**论文链接：**
http://www.zdoubleleaves.cn/paper/Understanding%20People%20Lifestyles%EF%BC%9AConstruction%20of%20Urban%20Movement%20Knowledge%20Graph%20from%20GPS%20Trajectory.pdf
## KnowledgeGraphConstruction
​	论文第3节的内容，工作分为以下几个部分
### 数据预处理

### 生成矩阵T和矩阵S
​	生成S矩阵，选择三个热门地点进行可视化。
![热门地点访问频率](https://github.com/zHaOshuAnGye/KGofGPS/blob/master/%E7%94%9F%E6%88%90T%E7%9F%A9%E9%98%B5%E5%92%8CS%E7%9F%A9%E9%98%B5/%E7%83%AD%E9%97%A8%E5%9C%B0%E7%82%B9%E8%AE%BF%E9%97%AE%E6%AC%A1%E6%95%B0%E5%91%A8%E6%9C%AB.PNG)

计算地点之间的马尔可夫一步转移概率矩阵T，T矩阵规格是2500*2500

| 文件名                        | 说明                                                         |
| :---------------------------- | ------------------------------------------------------------ |
| add_grid_and_time.py          | 预处理，生成trajectory.csv文件               |
| generateS.py                  | 基于trajectory.csv文件生成S矩阵                              |
| generateT.py                  | 基于trajectory.csv文件生成T矩阵                              |
| splite_trajectory.py          | 生成tj_id字段。根据时间将原数据集的点划分成若干个数据点的集合，每个集合的代表一条轨迹的所有点，每个集合的编号是tj_id. |
| visual.py                     | 可视化，展示所有数据的时间分布                               |
| visual2.py                    | 可视化，生成论文3.1节右上角的图的代码                        |
| S.txt                         | S是地点和频率矩阵。该文件是使用numpy.savetxt保存的S矩阵      |
| T.txt                         | T是网格之间的马尔可夫转移概率矩阵。该文件使用numpy.savetxt保存的T矩阵 |
| 热门地点访问次数整周/周末.PNG | 论文3.1节右上角的图                                          |
| 时间分布.PNG                  | 展示了所有周小时hour_in_week在数据中的分布                   |
| trajectory.csv                | 处理好的轨迹数据。字段有：id,time,longitude,latitude,grid_num,weekday,hour,hour_in_week,tj_id，其中id是车辆的编号，time是轨迹的时间，grid_num表示该点属于的网格号，weekday是根据time衍生出的判断星期的字段（周六为0，周日为1，周一为2，周二为3……），hour是截取了time中的小时数，hour_in_week表示转换之后的周小时（hour_in_week = hour+weekday*24），tj_id代表改点所属于的轨迹编号 |

### 生成矩阵Vt和矩阵Vs
利用非负矩阵分解生成Vt和Vs

| 文件名  | 说明                             |
| :------- | -------------------------------- |
| NMF.py  | 使用非负矩阵分解对S、T进行分解   |
| RSVD.py | 使用正则化SVD矩阵分解对T进行分解 |



### 知识图谱可视化
对于已经有的知识图谱关系T，按照论文4.4进行可视化处理

| 文件名                         | 说明                                                        |
| :---------------------------- | ------------------------------------------------------------ |
| filterT.py                    | 读取T.csv文件（就是上面的T.txt）并选择关系密切的地点对并打印      |
| trans.py                      | 将标准经纬度坐标转化为百度地图坐标                               |
| T.html                        | 仿照4.4可视化内容的结果，将关系紧密的地区在百度地图上标出          |

由于T尚未经过3.3中方法的分解，地区关系看起来有些杂乱，但是有部分地区关系，比如机场高速通道一带已经很明显了，与论文中图4(c)一致。
后续得到T子矩阵后关系应该会更加明显。
