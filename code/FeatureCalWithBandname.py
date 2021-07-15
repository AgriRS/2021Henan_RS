import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
import warnings
from numpy import loadtxt

warnings.filterwarnings("ignore")
# 加载数据集

path = r"D:\2020SentinelData\GFDATA\FeatureExtracted\GF1_Merge.txt"
dataset = loadtxt(path, skiprows=1, delimiter=",") # 以','为分割符，跳过1行（标features那一行）

#Sentinel-2A
# x = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12',
#      'NDWI8', 'NDWI5','MNDWI' ,'IBIA', 'IBIB', 'NDBI', 'NDVI','DVI', 'RVI', 'EVI',
#      'SAVI', 'MSAVI', 'RNDVI', 'RE8ANDVI', 'REDNDVI', 'TVI', 'RRI1', 'RRI2', 'MSRre', 'CIre',
#      'LSWI', 'B8ASAVG', 'B8ACon', 'B8ACORR', 'B8AVAR', 'B8ASVAR', 'B8ADVAR', 'B8ADISS'];

#Gaofen PMS
x = ['B1', 'B2', 'B3', 'B4', 'DVI', 'EVI', 'MSAVI', 'NDVI', 'NDWI', 'RVI', 'SAVI',
     'contrast', 'Correlation', 'Dissimilarity', 'Entropy', 'Homogeneity', 'Mean', 'SecondMoment', 'Variance'];
print(len(x))

# X:自变量矩阵（特征对应的数据） y:因变量矩阵（根据数据得出的分类结果）
X = dataset[:,0:-1]
y = dataset[:,-1]

dtrain = xgb.DMatrix(X, label=y, feature_names=x)

param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 9


model = xgb.train(param, dtrain)                                 #XGBClassifier()


# 解决中文和负号显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 使显示图标自适应
plt.rcParams['figure.autolayout'] = True

plot_importance(model, title='特征重要性排序', xlabel='得分', ylabel='特征', grid=False)

plt.show()