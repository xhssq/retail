import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False

fulian4 = pd.read_excel('fulian4Data.xlsx')
df = pd.DataFrame(fulian4,columns=['content','times'])
# print(df['times'].dtypes)
df['times'] = pd.to_datetime(df['times'])
df = df.set_index('times')
s = pd.Series(df['content'],index=df.index)
data = df.resample('d').count()
data.to_csv('短评数量日期.csv',encoding='utf-8')
xh = pd.read_csv('短评数量日期.csv')
plt.figure(figsize=(9,8))
plt.plot(xh['times'],xh['content'],color = 'red',marker='o')
plt.xticks(rotation=45)
plt.xlabel('短评发表日期')
plt.ylabel('短评数量')
plt.title('用户发表短评数量随日期变化折线图')
plt.savefig('Task3.1.png')
plt.show()

