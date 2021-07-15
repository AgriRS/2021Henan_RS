from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
font_size = 12
legend_font_size = 10
plt.figure(figsize=(4,3), dpi= 300)

names_gf = [64, 128, 256, 512]
names_s2a = [32, 64, 128, 256]

y1_iou_WFS_GF = [52.2, 65.6, 81.1, 78.7]
y1_iou_FS_GF = [54.5, 67.5, 81.8, 79.4]

y1_iou_WFS_S2A = [57.5, 74.7, 81.4, 85]
y1_iou_FS_S2A = [57.9, 75.6, 81.6, 85.6]

# y1_time_WFS_GF = [16.77, 6.76, 5.38, 7.51]
# y1_time_FS_GF = [16.76, 6.74, 5.42, 7.52]
#
# y1_time_WFS_S2A = [14.07, 5.64, 2.57, 2.08]
# y1_time_FS_S2A = [15.34, 5.64, 2.49, 2.07]

# 14.07, 5.64, 2.57, 2.08
# 15.34, 5.64, 2.49, 2.07
#
# 16.77, 6.76, 5.38, 7.51
# 16.76, 6.74, 5.42, 7.52

names = [32, 64, 128, 256, 512]
x1 = range(len(names_s2a))
x2 = range(1, 5)
print(x1)
print(x2)
x = range(len(names))
#
#
plt.ylim(ymin = 50)
plt.ylim(ymax = 90)
# plt.ylim(ymin = 0)
# plt.ylim(ymax = 20)
#
plt.plot(x1, y1_iou_WFS_S2A, marker='o', ms=2, label= u'S-2A based on WFS', color='darkblue', linestyle='--', linewidth=1)
plt.plot(x1, y1_iou_FS_S2A, marker='o', ms=2, label= u'S-2A based on FS', color='darkblue', linewidth=1)
plt.plot(x2, y1_iou_WFS_GF, marker='o', ms=2, label= u'Gaofen based on WFS', color='black', linestyle='--', linewidth=1)
plt.plot(x2, y1_iou_FS_GF, marker='o', ms=2, label= u'Gaofen based on FS', color='black', linewidth=1)
# plt.plot(x1, y1_time_WFS_S2A, marker='o', ms=2, label= u'S-2A based on WFS', color='darkblue', linestyle='--', linewidth=1)
# plt.plot(x1, y1_time_FS_S2A, marker='o', ms=2, label= u'S-2A based on FS', color='darkblue', linewidth=1)
# plt.plot(x2, y1_time_WFS_GF, marker='o', ms=2, label= u'Gaofen based on WFS', color='black', linestyle='--', linewidth=1)
# plt.plot(x2, y1_time_FS_GF, marker='o', ms=2, label= u'Gaofen based on FS', color='black', linewidth=0.7)
#
plt.xticks(x, names, rotation=0, fontsize=font_size)
plt.yticks(fontsize=font_size)
plt.xlabel('x',fontsize=font_size)
plt.ylabel('y',fontsize=font_size)

#time result need set
# plt.yticks(range(0,21,5), fontsize=font_size)

# plt.legend()  # 让图例生效
# plt.legend(fontsize=legend_font_size, loc='best')
plt.xlabel(u"Input-size", horizontalalignment='right') #X轴标签Bands
# plt.ylabel("Average time for each epoch / minute") #Y轴标签
plt.ylabel("mIoU / %") #Y轴标签
plt.title("", fontsize = 20) #标题
plt.margins()
plt.subplots_adjust(bottom=0.15)
plt.savefig(r'D:\GF_OA and F1 score _font 12.jpg',dpi = 300, bbox_inches='tight')
plt.show()