import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False
data = pd.read_excel('评分随城市变化数据.xlsx')
plt.figure(figsize=(9,8))
plt.plot(data['citys'],data['scores'],color = 'red',marker='o')
plt.xticks(rotation=45)
plt.xlabel('城市')
plt.ylabel('评分')
plt.title('不同城市评分变化情况')
plt.savefig('Task4.2.png')
plt.show()