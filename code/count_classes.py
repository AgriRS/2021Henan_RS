import gdal
import numpy as np
import matplotlib.pyplot as plt
import glob

# !----------  统计标签内各类别的数量 ---------------！#

#  初始化每个类的数目
Winter_wheat_num = 0
Greenhouse_num = 0
Garlic_num = 0
Urban_num = 0
Forestland_num = 0
Noncultivatedland_num = 0
OtherCrops_num = 0
Water_num = 0


label_paths = glob.glob(r'D:\2020SentinelData\GFDATA\clipSize\4_bands_imagelabel_256\*.png')
temp = 0
for label_path in label_paths:
    # label = gdal.Open(label_path).ReadAsArray(0, 0, 256, 256)
    label = gdal.Open(label_path).ReadAsArray(0, 0, 32, 32)
    # print(label)
    Winter_wheat_num += np.sum(label == 1)
    Greenhouse_num += np.sum(label == 2)
    Garlic_num += np.sum(label == 3)
    Urban_num += np.sum(label == 4)
    Forestland_num += np.sum(label == 5)
    Noncultivatedland_num += np.sum(label == 6)
    OtherCrops_num += np.sum(label == 7)
    Water_num += np.sum(label == 8)
    # Structure_num += np.sum(label == 9)
    # if Structure_num == 3:
    #     temp = Structure_num
    #
    #     print(Structure_num)
    #     print(label_path)
    # NakedLand_num += np.sum(label == 10)

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

classes = ('小麦', '大棚', '大蒜', '建设用地', '林地', '休闲耕地', '其他作物', '水体')
numbers = [Winter_wheat_num, Greenhouse_num, Garlic_num, Urban_num, Forestland_num, Noncultivatedland_num, OtherCrops_num, Water_num]
print(numbers)
plt.barh(classes, numbers)
plt.title('地物要素类别像素数目')
plt.savefig("地物要素类别像素数目图3.png", dpi = 300, bbox_inches="tight")
plt.show()