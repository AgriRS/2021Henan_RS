import matplotlib.pyplot as plt
# from matplotlib.pyplot import MultipleLocator
plt.figure(figsize=(10,8))
plt.rcParams['font.sans-serif'] = ['Times New Roman']
#epoch,train_loss1,mIoU1,time1,train_loss2,mIoU2,time2

#D:\2020SentinelData\LossandmIoU\BackBones\GFPMS  Sentinel2A
#efficientnet-b7  resnet50  timm-regnety-320 timm-resnest101e  vgg16

#D:\2020SentinelData\LossandmIoU\Sizes\GFPMS   64Size  128Size   512Size
input_txt = r'D:\2020SentinelData\LossandmIoU\BackBones\Sentinel2A\efficientnet-b7.txt'
x1 = []
x2 = []
yloss_1 = []
yloss_2 = []
ymiou_1 = []
ymiou_2 = []
f = open(input_txt)

for line in f:
    line = line.strip('\n')
    line = line.split(',')
    print(line)


    if line[1] != '':
        if line[3] != '':
            x1.append(int(line[0]))
            x2.append(int(line[0]))
            yloss_1.append(float(line[1]))
            ymiou_1.append(float(line[2]))
            yloss_2.append(float(line[3]))
            ymiou_2.append(float(line[4]))
        else:
            x1.append(int(line[0]))
            yloss_1.append(float(line[1]))
            ymiou_1.append(float(line[2]))
    else:
        x2.append(int(line[0]))
        yloss_2.append(float(line[3]))
        ymiou_2.append(float(line[4]))

f.close

#Sentinel  0.35-0.8 Timm-RegNetY-320 0.3
plt.ylim(ymin = 0.35)
plt.ylim(ymax = 0.8)

# ax=plt.gca()
# x_major_locator=MultipleLocator(10)
# ax.xaxis.set_major_locator(x_major_locator)
print(x1)
print(x2)
print(yloss_1)
print(yloss_2)
plt.plot(x1, yloss_1, marker='o', ms=0, label= u'Loss_WFC', color='tomato', linestyle='-', linewidth=3)
plt.plot(x1, ymiou_1, marker='o', ms=0, label= u'mIoU_WFC', color='#1677bb', linestyle='-', linewidth=3)
plt.plot(x2, yloss_2, marker='o', ms=0, label= u'Loss_FC', color='darkred', linewidth=3)
plt.plot(x2, ymiou_2, marker='o', ms=0, label= u'mIoU_FC', color='b',linewidth=3)
plt.xticks(x2[0:len(x2):2], x2[0:len(x2):2], rotation=0)

xMax = max(x2)
plt.xticks(range(0,xMax,3), fontsize=22)
plt.yticks(fontsize=22)
plt.xlabel('x', fontsize=22)
plt.ylabel('y', fontsize=22)

plt.margins(0)
plt.legend()  # 让图例生效
plt.legend(fontsize=22)

plt.xlabel("Epoch", fontsize=22)
plt.ylabel("Epoch average time / minute", fontsize=12)
#EfficientNet-b7  ResNet50  Timm-RegNetY-320 Timm-ResNest101e  VGG16
#Input-size: 64×64

plt.title("Patch size", fontsize=28, y = 0.92)
plt.tick_params(axis="both")
plt.rcParams['savefig.dpi'] = 300  # 图片像素

# plt.rcParams['figure.dpi'] = 200  # 分辨率

# plt.rcParams['figure.figsize'] = (10, 10)  # 尺寸
plt.show()
