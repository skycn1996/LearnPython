#include=utf-8 
from pyecharts import Line
attr = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
v1 = [11.0,12.1,30.2,19.4,29.5,186.0,123.7,194.8,186.9,37.1,11.8,29.12]
v2 = [2.6,5.9,9.0,26.4,28.7,70.7,175.6,182.2,48.7,18.8,6.0,2.3]
line= Line("变化折线图","precipitation and evaporation 一年的情况")
line.add("precipitation",attr,v1,mark_line=["average"],mark_point=["max","min"])
line.add("evaporation",attr,v2,mark_line=["average"],mark_point=["max","min"])
line.render()
