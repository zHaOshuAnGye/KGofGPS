# KGofGPS
复现论文**《UnderstandingPeopleLifestyles: ConstructionofUrbanMovementKnowledge GraphfromGPSTrajectory》**的工作内容
http://www.zdoubleleaves.cn/paper/Understanding%20People%20Lifestyles%EF%BC%9AConstruction%20of%20Urban%20Movement%20Knowledge%20Graph%20from%20GPS%20Trajectory.pdf
## KnowledgeGraphConstruction
论文第3节的内容，工作分为以下几个部分
### 数据预处理

### 生成矩阵T和矩阵S

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

