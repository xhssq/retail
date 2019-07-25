import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False

fulian4 = pd.read_excel('fulian4Data.xlsx')
# print(df['times'].dtypes)
df = pd.DataFrame(fulian4,columns=['scores','times'])
df['times'] = pd.to_datetime(df['times'])
df = df.set_index('times')
s = pd.Series(df['scores'],index=df.index)
data =df.resample('d').mean()
print(df.resample('d').count())
print(data)
data.to_csv('评分随日期变化数据.csv',encoding='utf-8')
xh = pd.read_csv('评分随日期变化数据.csv')
plt.figure(figsize=(9,8))
plt.plot(xh['times'][0:10],xh['scores'][0:10],color = 'red',marker='o')
plt.xticks(rotation=45)
plt.xlabel('用户短评发表日期')
plt.ylabel('用户评分')
plt.title('前10日用户评分随日期变化折线图')
plt.savefig('Task3.3.png')
plt.show()
