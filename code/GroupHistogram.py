# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Times New Roman']   # 用黑体显示中文
# plt.rcParams['axes.unicode_minus']=False     # 正常显示负号

x = np.array(["B","SWIR2","SWIR1","RE2","RE3","R","NIR","RE1","RE4","R","",
              "MNDWI","NDWI5","IBIB","NDWI8","IBIA","",
              "EVI","DVI","NDVI","SAVI","MSAVI","",
              "TVI","RENDVI","RE4NDVI","RNNDVI","LSWI","",
              "CORR","SAVG","DISS","DAVR","CON","SVAR","VAR"])  # x值取默认值
y = np.array([218,175,160,150,136,95,74,67,64,52,0,
              139,136,122,111,79,0,
              74,41,32,26,11,0,
              130,110,104,70,66,0,
              227,165, 118,116,75,18,12
              ])

# x = np.array(["B","NIR","G","R","",
#               "EVI","NDWI8","MSAVI","DVI","NDVI","",
#               "MEAN","VAR","CORR","CON","ENT","HOM","SM","DISS"])  # x值取默认值
# y = np.array([232,165,125,123,0,
#               309,146,102,79,21,0,
#               236,165, 136,119,113,94,50,16
#               ])

# sortIndex = np.argsort(-y) # 倒序，返回排序后各数据的原始下标

# x_sort = x[x] # 重新进行排序，与y保持初始顺序一致
# y_sort = y[x] # 重新进行排序，倒序

#定义函数来显示柱状上的数值
# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
        # plt.text(rect.get_x()+rect.get_width()/2.-0.25, 1.01*height, '%s' % int(height))

plt.xticks(np.arange(len(x)), x)
a = plt.bar(np.arange(len(x)),y,color=['steelblue','steelblue','steelblue','steelblue','steelblue','steelblue','steelblue','#636363','#636363','#636363','white',
                                       'steelblue','#636363','steelblue','#636363','#636363','white',
                                       'steelblue','#636363','#636363','#636363','#636363','white',
                                       'steelblue','steelblue','steelblue','#636363','#636363','white',
                                       'steelblue','steelblue','#636363','#636363','#636363','#636363','#636363'])

# a = plt.bar(np.arange(len(x)),y,color=['steelblue','steelblue','steelblue','steelblue','white',
#                                        'steelblue','steelblue','#636363','#636363','#636363','white',
#                                        'steelblue','steelblue','steelblue','#636363','#636363','#636363','#636363','#636363'])
# a = plt.bar(np.arange(len(x)),y,color=['#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','#669cd5','white',
#                                        '#f9bf00','#f9bf00','#f9bf00','#f9bf00','#f9bf00','white',
#                                        'bisque','bisque','bisque','bisque','bisque','white',
#                                        '#78ac48','#78ac48','#78ac48','#78ac48','#78ac48','white',
#                                        '#636363','#636363','#636363','#636363','#636363','#636363','#636363'])
# autolabel(a)

plt.subplots_adjust()
plt.margins()


plt.xticks(fontsize=16, rotation=45)
plt.yticks(fontsize=18)
plt.xlabel('', fontsize=16)
plt.ylabel('', fontsize=18)
# plt.xticks(x, names, rotation=0)

plt.title('')
# plt.ylabel('', fontsize=12)
# plt.xlabel('', fontsize=12)

plt.rcParams['savefig.dpi'] = 300
plt.show()