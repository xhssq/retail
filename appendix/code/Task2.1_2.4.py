import matplotlib.pyplot as plt
import jieba
import pandas as pd
from wordcloud import WordCloud
all_words =[]
with open('result.txt','r',encoding='utf-8') as f:
    comments = f.read()
comments = comments.split()
data_cut = [jieba.lcut(x) for x in  comments]
#利用jieba对短评数据进行分词
#print(data_cut[:5])
with open('stoplist.txt','r',encoding='utf-8') as f:
    stop = f.read()
stop = stop.split()
stop = [' '] + stop
data_after = [[j for j in i if j not in stop]for i in data_cut]
#去除停用词
#print(data_after)
for i in  data_after:
    all_words.extend(i)
num = pd.Series(all_words).value_counts()
print(num)
#统计去除停用词后的短评中的词语的词频
pic = plt.imread('aixin.jpg')

wc = WordCloud(background_color='white',font_path='C:\\Windows\\Fonts\\simhei.TTF',mask=pic)
wc2 = wc.fit_words(num)
plt.imshow(wc2)
plt.axis('off')
plt.savefig('images1.png',format='png')
plt.show()
#利用词频绘制词云