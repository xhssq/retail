import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False

fulian4 = pd.read_excel('fulian4Data.xlsx')
# print(df['times'].dtypes)
df = pd.DataFrame(fulian4,columns=['scores','citys'])
data = pd.pivot_table(df[['citys','scores']],index='citys',aggfunc=np.mean)
data.to_excel('评分随城市变化数据.xlsx',encoding='utf-8')
