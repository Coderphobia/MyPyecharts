#!/usr/bin/env python
# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from pyecharts import Map, Geo

# 世界地图数据
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]

# 省和直辖市
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}
provice=list(province_distribution.keys())
values=list(province_distribution.values())

# 城市 -- 指定省的城市 xx市
city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市', '信阳市', '新乡市']
values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

# 区县 -- 具体城市内的区县  xx县
quxian = ['夏邑县', '民权县', '梁园区', '睢阳区', '柘城县', '宁陵县']
values3 = [3, 5, 7, 8, 2, 4]


map0 = Map("世界地图示例", width=1200, height=600)
map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
map0.render(path="世界地图.html")

# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("中国地图",'中国地图', width=1200, height=600)
map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,
    visual_text_color='#000')
map.show_config()
map.render(path="中国地图.html")

# 河南地图  数据必须是省内放入城市名
map2 = Map("河南地图",'河南', width=1200, height=600)
map2.add('河南', city, values2, visual_range=[1, 10], maptype='河南', is_visualmap=True, visual_text_color='#000')
map2.show_config()
map2.render(path="河南地图.html")

# # 商丘地图 数据为商丘市下的区县
map3 = Map("商丘地图",'商丘', width=1200, height=600)
map3.add("商丘", quxian, values3, visual_range=[1, 10], maptype='商丘', is_visualmap=True,
    visual_text_color='#000')
map3.render(path="商丘地图.html")




from pyecharts import WordCloud

name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud =WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render(path='权重词云.html')


wordcloud2 =WordCloud(width=1300, height=620)
wordcloud2.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud2.show_config()
wordcloud2.render(path='变形词云.html')


from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.show_config()
bar.render(path='bar.html')


from pyecharts import EffectScatter
v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("带有涟漪特效动画的动态散点图示例")
es.add("effectScatter", v1, v2)
es.render("effect_scatter.html")

from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.render("pie.html")


from pyecharts import Gauge
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.show_config()
gauge.render("gauge.html")



from pyecharts import Line, Overlap, Bar

attr = ['A', 'B', 'C', 'D', 'E', 'F']

v1 = [10, 20, 30, 40, 50, 60]
v2 = [38, 28, 58, 48, 78, 68]

bar = Bar('Line-Bar')
bar.add('bar', attr, v1)
line = Line()
line.add('line', attr, v2)

overlap = Overlap()
overlap.add(bar)
overlap.add(line)

overlap.render('bar-line.html')


