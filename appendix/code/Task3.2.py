import pandas as pd
import matplotlib.pyplot as plt
from pandas import to_datetime
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimHei'
#plt.rcParams['axcs.unicode_minus'] = False

fulian4 = pd.read_excel('fulian4data.xlsx')
df = to_datetime((fulian4['times']))
hour = df.dt.hour
count = []
h= []
arrange = np.array(hour)
time = np.unique(arrange)
for i in time:
    mask = (arrange == i)
    arrange_new = arrange[mask]
    s = arrange_new.size
    count.append(s)
    h.append(i)
print(count,h)

plt.figure(figsize=(9,8))
plt.plot(h,count,color = 'red',marker='o')
plt.xticks(rotation=45)
plt.xlabel('短评发表的时刻')
plt.ylabel('短评数量')
plt.title('用户发表短评数量随时刻变化折线图')
plt.savefig('Task3.2.png')
plt.show()