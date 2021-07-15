# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
font_size = 12
legend_font_size = 8
plt.figure(figsize=(16,9), dpi= 300)
# names = ['B', 'G', 'R', 'RE1', 'RE2', 'RE3', 'NIR', 'RE4', 'SWIR1', 'SWIR2']
# names = ['B', 'G', 'R', 'NIR']
names = ['Site F in 2019', 'Site D in 2020', 'Site E in 2021', 'Site F in 2021']
x = range(len(names))

# y = [727.0474906, 914.7323015, 918.4223704, 1216.277596, 2474.617906,
#      3313.619429, 3546.20982, 3438.411517, 1803.728962, 1362.208165]
# y1 = [371.5986073, 411.7879444, 569.8447625, 521.7765774, 383.0036287,
#      765.8683014, 851.5981815, 801.3306932, 680.3340815, 806.1046866]

# y1_128_OA = [0.793218613, 0.693424702, 0.865298271, 0.828225308]
# y1_128_F1 = [0.533300603, 0.579099119, 0.628856512, 0.663195995]
# y1_256_OA = [0.837598085, 0.771692276, 0.872388363, 0.847617001]
# y1_256_F1 = [0.581806756, 0.565945045, 0.67008222, 0.690435003]
# y2_128_OA = [0.888284683, 0.830911875, 0.919143438, 0.808087111]
# y2_128_F1 = [0.578735765, 0.577640869, 0.720543631, 0.592602546]
# y2_256_OA = [0.972788095, 0.970380306, 0.977203846, 0.968622208]
# y2_256_F1 = [0.813126173, 0.75758014, 0.854991253, 0.820563148]
y1_128_OA = [79.3218613, 69.3424702, 86.5298271, 82.8225308]
y1_256_OA = [78.37598085, 77.1692276, 87.2388363, 84.7617001]
y2_128_OA = [88.8284683, 83.0911875, 91.9143438, 80.8087111]
y2_256_OA = [97.2788095, 97.0380306, 97.7203846, 96.8622208]

y1_128_F1 = [53.3300603, 57.9099119, 62.8856512, 66.3195995]
y1_256_F1 = [58.1806756, 56.5945045, 67.008222, 69.0435003]
y2_128_F1 = [57.8735765, 57.7640869, 72.0543631, 59.2602546]
y2_256_F1 = [81.3126173, 75.758014, 85.4991253, 82.0563148]


# plt.ylim(ymin = 300)
# plt.ylim(ymax = 3700)

plt.ylim(ymin = 50)
plt.ylim(ymax = 100)

plt.plot(x, y1_128_OA, marker='o', ms=4, color='gray', label=u'128_OA_WFS')#, mec='b', mfc='w',label=u'Mean') #控制符号大小的 ms=10,
plt.plot(x, y1_256_OA, marker='o', ms=4, color='dodgerblue', label=u'256_OA_WFS')#, mec='b', mfc='w',label=u'Mean')
plt.plot(x, y2_128_OA, marker='o', ms=4, color='green', label=u'128_OA_FS')#, mec='b', mfc='w',label=u'Mean')
plt.plot(x, y2_256_OA, marker='o', ms=4, color='red', label=u'256_OA_FS')#, mec='b', mfc='w',label=u'Mean')

plt.plot(x, y1_128_F1, marker='+', ms=4, color='gray', label=u'128_F1_WFS', linestyle='--')#, mec='gray', label=u'Standard deviation')
plt.plot(x, y2_128_F1, marker='+', ms=4, color='green', label=u'128_F1_FS', linestyle='--')
plt.plot(x, y1_256_F1, marker='+', ms=4, color='dodgerblue', label=u'256_F1_WFS', linestyle='--')
plt.plot(x, y2_256_F1, marker='+', ms=4, color='red', label=u'256_F1_FS', linestyle='--')

# for i in range(len(y2_256_OA)):
#     plt.text(x[i], y2_256_OA[i], '%s' %round(y2_256_OA[i],2), ha='center', fontsize=font_size, va='top')
# for i in range(len(y2_256_F1)):
#     plt.text(x[i], y2_256_F1[i], '%s' %round(y2_256_F1[i],2), ha='center', fontsize=font_size, va='top')
#
# for i in range(len(y2_256_OA)):
#     plt.text(x[i], y2_256_OA[i], '%s' %round(y2_256_OA[i]*100,2)+'%', ha='center', fontsize=10)
# for i in range(len(y2_256_F1)):
#     plt.text(x[i], y2_256_F1[i], '%s' %round(y2_256_F1[i]*100,2)+'%', ha='center', fontsize=10, va='bottom')


plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
plt.xlabel('x',fontsize=font_size)
plt.ylabel('y',fontsize=font_size)


plt.legend()  # 让图例生效
plt.legend(fontsize=legend_font_size)
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"") #X轴标签Bands
plt.ylabel("") #Y轴标签
plt.title("") #标题
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# plt.rcParams['figure.figsize'] = (15.0, 8.0)  # 尺寸
plt.margins(0.1)
plt.subplots_adjust()
plt.savefig(r'D:\image_name.jpg', bbox_inches='tight')
plt.show()