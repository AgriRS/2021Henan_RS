import gdal
import os
import numpy as np

#先读取一景高分的数据
#读取影像数据 read Gaofen tif file
def readTif(filename):
    dataset = gdal.Open(filename)
    if dataset ==None:
        print(filename+"File open failed !")
    return dataset


#----------------------NDVI = (nir-r)/(nir+r)
def NDVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    #强制转换成32位的 conver to float 32 bit
    nir = dataset.GetRasterBand(4).ReadAsArray(0,0,cols,rows).astype(np.float32)
    red  =dataset.GetRasterBand(3).ReadAsArray(0,0,cols,rows).astype(np.float32)
    #不能除以0值，要去除这些东西 remove 0 value
    NDVI = (nir-red)/(nir+red)

    NDVI[np.isnan(NDVI)] = 0  # 过滤异常值 Filter outliers

    #把空值都附成0  set null to 0
    NDVI[np.isnan(NDVI)] = 0
    NDVI.astype(np.float32)
    # print(NDVI)
    NDVIname = "NDVI"
    return NDVI,NDVIname


#------------NDWI = (green-nir)/(green+nir)
def NDWI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    #强制转换成32位的
    green = dataset.GetRasterBand(2).ReadAsArray(0,0,cols,rows).astype(np.float32)
    nir  =dataset.GetRasterBand(4).ReadAsArray(0,0,cols,rows).astype(np.float32)
    NDWI = (green-nir)/(green+nir)
    # 把空值都附成0
    NDWI[np.isnan(NDWI)] = 0
    NDWI.astype(np.float32)
    NDWIname = "NDWI"
    return NDWI,NDWIname


#------------DVI = nir-red
def DVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    #强制转换成32位的
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir  =dataset.GetRasterBand(4).ReadAsArray(0,0,cols,rows).astype(np.float32)
    DVI = nir-red
    # 把空值都附成0
    DVI[np.isnan(DVI)] = 0
    DVI.astype(np.float32)
    DVIname = "DVI"
    return DVI,DVIname

#------------RVI = nir/red
def RVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    #强制转换成32位的
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir  =dataset.GetRasterBand(4).ReadAsArray(0,0,cols,rows).astype(np.float32)
    RVI = nir/red
    # 把空值都附成0
    RVI[np.isnan(RVI)] = 0
    RVI.astype(np.float32)
    RVIname = "RVI"
    return RVI,RVIname

#-----------SAVI = ((nir-r)/(nir+r+0.5))*1.5
def SAVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    SAVI = ((nir-red)/(nir+red+5000))*1.5
    # 把空值都附成0
    SAVI[np.isnan(SAVI)] = 0
    SAVI.astype(np.float32)
    SAVIname = "SAVI"
    return SAVI,SAVIname

#-----------------EVI = 2.5*(nir-r)/(nir+6*r-7.5*blue+1)
def EVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    blue = dataset.GetRasterBand(1).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    np.seterr(divide='ignore', invalid ='ignore')
    EVI = 2.5 * (nir - red) / (nir + 6.0 * red - 7.5 * blue + 10000.0)
    # 把空值都附成0
    EVI[np.isnan(EVI)] = 0
    EVI.astype(np.float32)
    EVIname = "EVI"
    return EVI,EVIname

#-------------------MSAVI-----------
def MSAVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    # blue = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float32)
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    #((2 * NIR + 1) - sqrt((2 * NIR +1) *(2 * NIR +1) + 8 *(NIR - RED)))/2
    MSAVI = ((2 * nir + 10000) - np.sqrt((2 * nir +10000) *(2 * nir +10000) + 8 *(nir - red)))/2
    # 把空值都附成0
    MSAVI[np.isnan(MSAVI)] = 0
    MSAVI.astype(np.float32)
    MSAVIname = "MSAVI"
    return MSAVI,MSAVIname

#-------------------EVI-2-----------
def EVI2(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    blue = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float32)
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    EVI2 = 2.5 * (nir - red) / (nir + 6.0 * red + 2.4 * blue + 10000.0)
    # 把空值都附成0
    EVI2[np.isnan(EVI2)] = 0
    EVI2.astype(np.float32)
    EVI2name = "EVI2"
    return EVI2,EVI2name

#-----------------GNDVI----------------
def GNDVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    green = dataset.GetRasterBand(2).ReadAsArray(0,0,cols,rows).astype(np.float32)
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    GNDVI = (nir - green) / (nir + green)
    # 把空值都附成0
    GNDVI[np.isnan(GNDVI)] = 0
    GNDVI.astype(np.float32)
    GNDVIname = "GNDVI"
    return GNDVI,GNDVIname
# #MSAVI
# def MSAVI(dataset):
#     cols = dataset.RasterXSize
#     rows = dataset.RasterYSize
#     # 强制转换成32位的
#     blue = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float32)
#     red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
#     nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
#     MSAVI = 2 * nir +1 +np.sqrt((2*nir+1)**2)-
#     # 把空值都附成0
#     MSAVI[np.isnan(MSAVI)] = 0
#     MSAVI.astype(np.float32)
#     MSAVIname = "MSAVI"
#     return MSAVI,MSAVIname
#OSAVI
def OSAVI(dataset):
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    # 强制转换成32位的
    blue = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float32)
    red = dataset.GetRasterBand(3).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    nir = dataset.GetRasterBand(4).ReadAsArray(0, 0, cols, rows).astype(np.float32)
    OSAVI = 1.16 * nir/10000 - red / nir + red/10000 + 0.16
    # 把空值都附成0
    OSAVI[np.isnan(OSAVI)] = 0
    OSAVI.astype(np.float32)
    OSAVIname = "OSAVI"
    return OSAVI,OSAVIname
#写入影像数据
def writeTiff(Savepath,VIindex,data,QZ,VIname):
    # 先不这样写，多加个形参让他自己调吧
    driver = gdal.GetDriverByName("GTiff")
    output_path = Savepath+QZ+"_"+VIname+".tif"
    if os.path.exists(output_path):
        os.remove(output_path)

    output = driver.Create(output_path,VIindex.shape[1],VIindex.shape[0],bands=1,eType = gdal.GDT_Float32)

    output.SetProjection(data.GetProjection())
    output.SetGeoTransform(data.GetGeoTransform())
    # print('-----------------------------------')
    # print(VIindex)
    # print('-----------------------------------')
    output2 = output.GetRasterBand(1).WriteArray(VIindex)
    return output2

# def os_data(image_path,data_folder):
#
#     for i in range(len(image_path)):
#         #QZ是字符串
#         QZ = os.path.splitext(image_path[i])[0]
#         print(type(QZ))
#         HZ = os.path.splitext(image_path[i])[1]
#         if (HZ == ".tif"):
#             image = data_folder + "/" + image_path[i]
#             print(image)
#             data = readTif(image)
#             print(type(data))
#     # return data,QZ

if __name__ == '__main__':
    # 加载影像的路径
    # 分别写文件夹的路径和文件路径，然后连接起来
    # 文件夹路径
    # file_path = "H:/GFdata/GF1dataprocess/GF_process"
    #file_path = "H:/GFdata/qingshuihe_clip"
    # test_image_paths = glob.glob('../tcdata/suichang_round1_test_partA_210120/*.tif')
    file_path = r'D:/2020SentinelData/111'

    image_path = os.listdir(file_path)
    print(image_path)
    # 定义一个输出路径
    # 写一个文件夹的路径，主要是想试下批量
    #啊这，没有这个路径

    # ndwi8 ndvi  dvi evi rvi savi msavi
    savepath = "H:/GFdata/GF1dataprocess/results/"
    NDWIpath = r"D:/2020SentinelData/2021/ndwi8/"
    NDVIpath = r"D:/2020SentinelData/GFDATA/VIcal/NDVI/"
    DVIpath = r"D:/2020SentinelData/GFDATA/VIcal/DVI/"
    EVIpath = r'D:/2020SentinelData/2021/evi/' #r"D:/2020SentinelData/GFDATA/VIcal/EVI/"
    RVIpath = r'D:/2020SentinelData/GFDATA/VIcal/RVI/'
    SAVIpath = r'D:/2020SentinelData/GFDATA/VIcal/SAVI/'
    MSAVIpath = r'D:/2020SentinelData/GFDATA/VIcal/MSAVI/'
    '''
    发现一个问题，data嵌套在writeTiff里边了，这样不利于程序的独立性，还得再改改，通过for循环提取影像是写在主程序里呢，还是新写一个批处理的函数
    通过实践发现，放在独立的函数值时，data作为一个局部变量，没法返回值，就不行
    试了一下，写在主函数里，效果还行，就是那几个指数的程序要稍微改下条件，不然读出来的值不对
    '''
    #写一下要调用的几个指数
    # 把循环写在主程序里试一下
    for i in range(len(image_path)):
        QZ = os.path.splitext(image_path[i])[0]
        HZ = os.path.splitext(image_path[i])[1]
        if HZ == '.tif':
            image = file_path+"/"+image_path[i]
            data = readTif(image)
            print(image)

            NDWI_index, NDWIname = NDWI(data)
            NDVI_index,NDVIname = NDVI(data)
            DVI_index, DVIname = DVI(data)
            EVI_index, EVIname = EVI(data)
            RVI_index, RVIname = RVI(data)
            SAVI_index,SAVIname = SAVI(data)
            MSAVI_index,MSAVIname = MSAVI(data)

            NDWI_data = writeTiff(NDWIpath, NDWI_index, data, QZ, NDWIname)
            NDVI_data = writeTiff(NDVIpath,NDVI_index,data,QZ,NDVIname)
            DVI_data = writeTiff(DVIpath, DVI_index, data, QZ, DVIname)
            EVI_data = writeTiff(EVIpath, EVI_index, data, QZ, EVIname)
            RVI_data = writeTiff(RVIpath, RVI_index, data, QZ, RVIname)
            SAVI_data = writeTiff(SAVIpath,SAVI_index,data,QZ,SAVIname)
            MSAVI_data = writeTiff(MSAVIpath,MSAVI_index,data,QZ,MSAVIname)
    # data = os_data(image_path,file_path)
    # NDVI_index = NDVI(data)
    # EVI_index = EVI(data)


