from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
font_size = 12
legend_font_size = 12
plt.figure(figsize=(16,9), dpi= 300)
#S_2A
names = ['Site F in 2019', 'Site D in 2020', 'Site E in 2021', 'Site F in 2021']
#Gaofen
# names = ['Part F in 2019', 'Part B in 2020', 'Part E in 2021', 'Part F in 2021']
x = range(len(names))
#S_2A results
y1_128_OA = [79.3218613, 69.3424702, 86.5298271, 82.8225308]  #10 bands
y2_128_OA = [88.8284683, 83.0911875, 91.9143438, 80.8087111]  #15 bands
y1_256_OA = [78.37598085, 77.1692276, 87.2388363, 84.7617001] #10 bands
y2_256_OA = [97.2788095, 97.0380306, 97.7203846, 96.8622208]  #15 bands

y1_128_F1 = [53.3300603, 57.9099119, 62.8856512, 66.3195995] #10 bands
y2_128_F1 = [57.8735765, 57.7640869, 72.0543631, 59.2602546] #15 bands
y1_256_F1 = [58.1806756, 56.5945045, 67.008222, 69.0435003]  #10bands
y2_256_F1 = [81.3126173, 75.758014, 85.4991253, 81.91804011]  #15bands

#gaofen results
# y1_256_OA = [64.37826993, 92.9177736, 78.76744967, 76.40909117] #4 bands
# y2_256_OA = [75.58904949, 97.72468701, 87.65776834, 91.16924799]  #9 bands
#
# y1_256_F1 = [52.56294297, 50.32673991, 50.51141082, 36.86917124]   #4 bands
# y2_256_F1 = [65.20041808, 74.75376718, 67.53245548, 66.44861103]   #9 bands


plt.ylim(ymin = 50)
plt.ylim(ymax = 100)
marker_s = 40
plt.scatter(x, y1_128_OA, marker='o', s=marker_s, color='black', label=u'128_OA_WFS')#, mec='b', mfc='w',label=u'Mean') #控制符号大小的 ms=10,
plt.scatter(x, y1_256_OA, marker='o', s=marker_s, color='blue', label=u'128 input-size: 256 input-size: ')#, mec='b', mfc='w',label=u'Mean')
plt.scatter(x, y2_128_OA, marker='o', s=marker_s, color='green', label=u'128_OA_FS')#, mec='b', mfc='w',label=u'Mean')
plt.scatter(x, y2_256_OA, marker='o', s=marker_s, color='red', label=u'OA based on FS   OA based on WFS ')#, mec='b', mfc='w',label=u'Mean')

plt.scatter(x, y1_128_F1, marker='+', s=60, color='black', label=u'128_F1_WFS')#, linestyle='--')#, mec='gray', label=u'Standard deviation')
plt.scatter(x, y1_256_F1, marker='+', s=marker_s, color='blue', label=u'F1-score based on FS   F1-score based on WFS')#, linestyle='--')
plt.scatter(x, y2_128_F1, marker='+', s=40, color='green', label=u'128_F1_FS')#, linestyle='--')
plt.scatter(x, y2_256_F1, marker='+', s=marker_s, color='red', label=u'F1-score based on FS   F1-score based on WFS')#, linestyle='--')

label_font_size = 10
#
# #S-2A
for i in range(len(y1_128_OA)):
    plt.text(x[i]-0.28, y1_128_OA[i]+1, '%s' %round(y1_128_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='black')
for i in range(len(y1_256_OA)):
    if i > 0:
        plt.text(x[i] + 0.05, y1_256_OA[i] + 1.8, '%s' % round(y1_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')
    else:
        plt.text(x[i] + 0.05, y1_256_OA[i] + 0.6, '%s' % round(y1_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')

for i in range(len(y2_128_OA)):
    if i < 3:
        plt.text(x[i]+0.05, y2_128_OA[i]+1, '%s' %round(y2_128_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='green')
    else:
        plt.text(x[i] + 0.05, y2_128_OA[i] - 0.4, '%s' % round(y2_128_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='green')
for i in range(len(y2_256_OA)):
    plt.text(x[i]+0.05, y2_256_OA[i]+0.6, '%s' %round(y2_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
for i in range(len(y1_128_F1)):
    if i == 1:
        plt.text(x[i] + 0.05, y1_128_F1[i] + 2, '%s' % round(y1_128_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='black')
    else:
        plt.text(x[i]+0.05, y1_128_F1[i]+0.8, '%s' %round(y1_128_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='black')
for i in range(len(y1_256_F1)):
    if i == 1:
        plt.text(x[i] + 0.05, y1_256_F1[i] + 0.4, '%s' % round(y1_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')
    else:
        plt.text(x[i] + 0.05, y1_256_F1[i] + 0.8, '%s' % round(y1_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')

for i in range(len(y2_128_F1)):
    plt.text(x[i]-0.28, y2_128_F1[i]+0.8, '%s' %round(y2_128_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='green')
for i in range(len(y2_256_F1)):
    if i == 0:
        plt.text(x[i]+0.05, y2_256_F1[i]+1.2, '%s' %round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
    elif i == 1:
        plt.text(x[i] + 0.05, y2_256_F1[i] + 0.2, '%s' % round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
    elif i == 2:
        plt.text(x[i] + 0.05, y2_256_F1[i] + 0.2, '%s' % round(y2_256_F1[i], 2)+'0', ha='left', fontsize=label_font_size, va='top', color='red')
    elif i == 3:
        plt.text(x[i] + 0.05, y2_256_F1[i] + 1.2, '%s' % round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')


#Gaofen
# for i in range(len(y1_256_OA)):
#     if i == 0:
#         plt.text(x[i] + 0.05, y1_256_OA[i] - 0.2, '%s' % round(y1_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')
#     else:
#         plt.text(x[i] + 0.05, y1_256_OA[i] + 1.2, '%s' % round(y1_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')
#
# for i in range(len(y2_256_OA)):
#     plt.text(x[i]+0.05, y2_256_OA[i]+0.8, '%s' %round(y2_256_OA[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
#
#
# for i in range(len(y1_256_F1)):
#     plt.text(x[i] + 0.05, y1_256_F1[i] + 1.2, '%s' % round(y1_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='blue')
#
# for i in range(len(y2_256_F1)):
#     if i == 0:
#         plt.text(x[i]+0.05, y2_256_F1[i]+2.4, '%s' %round(y2_256_F1[i], 2) + '0', ha='left', fontsize=label_font_size, va='top', color='red')
#     elif i == 1:
#         plt.text(x[i] + 0.05, y2_256_F1[i] + 1.2, '%s' % round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
#     elif i == 2:
#         plt.text(x[i] + 0.05, y2_256_F1[i] + 1.2, '%s' % round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')
#     elif i == 3:
#         plt.text(x[i] + 0.05, y2_256_F1[i] + 1.2, '%s' % round(y2_256_F1[i], 2), ha='left', fontsize=label_font_size, va='top', color='red')


plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)
plt.xlabel('x',fontsize=font_size)
plt.ylabel('y',fontsize=font_size)


# plt.legend()  # 让图例生效
# plt.legend(fontsize=legend_font_size, loc='best')
# frame = legend.get_frame()
# frame.set_facecolor('white')
plt.xticks(x, names, rotation=0)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"") #X轴标签Bands
plt.ylabel("OA and F1-score / %") #Y轴标签
# plt.title("(a) (b)", fontsize = 20) #标题
plt.margins(0.1)
plt.subplots_adjust()
plt.savefig(r'D:\GF_OA and F1 score _font 12.jpg',dpi = 200, bbox_inches='tight')
plt.show()