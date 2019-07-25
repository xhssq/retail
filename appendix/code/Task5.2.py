import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from tkinter import _flatten
import re
plt.rcParams['font.sans-serif'] = 'SimHei'

data = pd.read_excel('fulian4Data.xlsx')
df = pd.DataFrame(data,columns=['scores','user-info'])

times = []
score = []
for i in range(0,len(df)):
    # i = str(i)
    times.append(re.findall(r'\d{4}-\d{2}-\d{2}', str(df['user-info'][i])))
# times = sum(times,[])
times = list(_flatten(times))
for j in range(0,len(df)):
    score.append(df['scores'][j])
del score[282]
df=pd.DataFrame(list(zip(score,times)),
                  columns=['scores','user-info'])
df['user-info'] = pd.to_datetime(df['user-info'])
# data_1 = pd.pivot_table(df[['user-info','scores']],index='user-info',aggfunc=np.mean)
# print(data_1)
df = df.set_index('user-info')
s = pd.Series(df['scores'], index=df.index)
data_1 = df.resample('AS').mean().to_period('A')
xh = pd.DataFrame(data_1)
xh.to_csv('会龄与分数.csv')
data_2 = pd.read_csv('会龄与分数.csv')
plt.figure(figsize=(9,8))
plt.plot(data_2['user-info'],data_2['scores'],color = 'red',marker='o')
plt.xticks(rotation=45)
plt.xlabel('用户加入豆瓣时间')
plt.ylabel('该年加入用户平均评分')
plt.title('评分随用户会龄变化折线图')
plt.savefig('Task5.2.png')
plt.show()


