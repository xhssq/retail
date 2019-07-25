import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font='SimHei',font_scale=1.0)  # 解决Seaborn中文显示问题并调整字体大小

sns.set_style('darkgrid')


data = pd.read_excel('fulian4Data.xlsx')
data ['user-info']= data['user-info']
work = []
for i in range(0,len(data)):
    # i = str(i)
    work.append(re.findall(r'\d{4}-\d{2}-\d{2}', str(data['user-info'][i])))
work = sum(work, [])
df=pd.DataFrame(list(zip(work)),
                  columns=['times'])
df.to_excel('时间分布.xlsx')
times = pd.read_excel('时间分布.xlsx')
times['times']=times['times']
Time=[]
for i in range(0,len(times)):
    Time.append(datetime.strptime(times['times'][i], '%Y-%m-%d'))
# sns.distplot(works['高峰小时'], color='#ff8000')
# plt.show()
emmm=[]
for i in range(0,len(Time)):
    emmm.append(Time[i].year)
print(emmm)
plt.figure(figsize=(9,8))
plt.xlabel('User Admission Time')
plt.ylabel('Proportion')
plt.title('Age distribution map')
sns.distplot(emmm, color='#ff8000')
plt.show()
# print(df)
# print(list)
# print(len(list))