import pandas as pd
import matplotlib.pyplot as plt
from pyecharts import Geo
data = pd.read_csv('常居城市分布数据.csv')
geo = Geo("豆瓣用户常居城市分布情况图",title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr = list(data['城市'])
# print(attr)
value = list(data['数量'])
# print(value)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True,maptype='china')
geo.show_config()
geo.render()