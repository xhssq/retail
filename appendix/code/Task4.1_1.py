import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import collections
plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False

fulian4 = pd.read_excel('fulian4Data.xlsx')
df = fulian4['citys']
dic = collections.Counter(df)
city = []
count = []
for key in dic:
    city.append(key)
    count.append(dic[key])
print(city,count)
data = pd.DataFrame(list(zip(city, count)),
                      columns=[ '城市','数量'])
data.to_csv('常居城市分布数据.csv',encoding='utf-8')
