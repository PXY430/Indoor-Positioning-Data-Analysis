import pandas as pd
import numpy as np

input_file = 'building_1_floor_3.csv'
data = pd.read_csv(input_file)


# 定义两条直线的参数
line1 = {'p1': np.array([-7539, 4864897]), 'p2': np.array([-7451, 4864848])}
line2 = {'p1': np.array([-7517, 4864836]), 'p2': np.array([-7476, 4864908])}

# 对每个点进行分类
data['partition'] = None
for i, row in data.iterrows():
    x = row['LONGITUDE']
    y = row['LATITUDE']

    if (x - line1['p1'][0]) * (line1['p2'][1] - line1['p1'][1]) - (y - line1['p1'][1]) * (line1['p2'][0] - line1['p1'][0]) >= 0 and \
       (x - line2['p1'][0]) * (line2['p2'][1] - line2['p1'][1]) - (y - line2['p1'][1]) * (line2['p2'][0] - line2['p1'][0]) <= 0:
        data.at[i, 'partition'] = 'building_1_floor_3(1)'
    elif (x - line1['p1'][0]) * (line1['p2'][1] - line1['p1'][1]) - (y - line1['p1'][1]) * (line1['p2'][0] - line1['p1'][0]) >= 0 and \
         (x - line2['p1'][0]) * (line2['p2'][1] - line2['p1'][1]) - (y - line2['p1'][1]) * (line2['p2'][0] - line2['p1'][0]) > 0:
        data.at[i, 'partition'] = 'building_1_floor_3(2)'
    elif (x - line1['p1'][0]) * (line1['p2'][1] - line1['p1'][1]) - (y - line1['p1'][1]) * (line1['p2'][0] - line1['p1'][0]) < 0 and \
         (x - line2['p1'][0]) * (line2['p2'][1] - line2['p1'][1]) - (y - line2['p1'][1]) * (line2['p2'][0] - line2['p1'][0]) <= 0:
        data.at[i, 'partition'] = 'building_1_floor_3(3)'
    else:
        data.at[i, 'partition'] = 'building_1_floor_3(4)'

# 分别保存四个部分的数据为CSV文件
output_folder = 'D:/Data/Building1/Floor3/'
for partition, group in data.groupby('partition'):
    group.drop('partition', axis=1, inplace=True)  # 移除分类列
    group.to_csv(output_folder + partition + '.csv', index=False)
