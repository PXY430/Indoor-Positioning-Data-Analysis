import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: 读取经纬度数据
data = pd.read_csv("building_1_floor_0.csv")

#修改经纬度
data['LONGITUDE'] = ((((data['LONGITUDE'] + 7400) * 0.2) * 0.1 +6) * 0.3-0.7) * 0.8
data['LATITUDE'] = (((data['LATITUDE'] - 486500) * 0.01 - 4) * 0.8 - 35024 + 0.7) * 0.7 + 0.05


#字体格式
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 11


# Step 2: 绘制位置图
plt.figure(figsize=(10, 8))
plt.scatter(data['LONGITUDE'], data['LATITUDE'], color='green', alpha=0.6)
plt.xlabel(' Normalized Longitude')
plt.ylabel('Normalized Latitude')
#plt.title('building_0_floor_0')

plt.ticklabel_format(style='plain', useOffset=False)

plt.grid(True)
plt.show()

#生成3维图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['LONGITUDE'], data['LATITUDE'], data['WAP001'], c='green', marker='o',s = 5) #s为点的大小
ax.set_xlabel(' Nomalized Longitude')
ax.set_ylabel('Normalized Latitude')
ax.set_zlabel('WAP001')
plt.show()
