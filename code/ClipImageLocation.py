from osgeo import gdal

# !----------  将图像和标签以固定size进行裁切，同时保持裁切后的标签空间投影和位置的正确 ---------------！#
# !----------  The image and label are clip in a fixed size, and the projection and position
# of the results are consistent with the original ---------------！#

class ClipImageByLocation:
    # 读图像文件 read tif data
    def read_img(self, filename):
        dataset = gdal.Open(filename)  # 打开文件 open file
        im_width = dataset.RasterXSize  # 栅格矩阵的列数 raster columns
        im_height = dataset.RasterYSize  # 栅格矩阵的行数 raster rows

        im_geotrans = dataset.GetGeoTransform()
        im_proj = dataset.GetProjection()
        im_data = dataset.ReadAsArray(0, 0, im_width, im_height)

        del dataset
        return im_proj, im_geotrans, im_data

    # 写文件，以写成tif为例 write tif file
    def write_img(self, filename, im_proj, origin_x, origin_y, pixel_width, pixel_height, im_data):
        # gdal数据类型包括
        # gdal.GDT_Byte,
        # gdal .GDT_UInt16, gdal.GDT_Int16, gdal.GDT_UInt32, gdal.GDT_Int32,
        # gdal.GDT_Float32, gdal.GDT_Float64
        # print(filename)

        # 判断栅格数据的数据类型  type of raster data
        if 'int8' in im_data.dtype.name:
            datatype = gdal.GDT_Byte
        elif 'int16' in im_data.dtype.name:
            datatype = gdal.GDT_UInt16
        else:
            datatype = gdal.GDT_Float32

        # 判读数组维数 bands
        if len(im_data.shape) == 3:
            im_bands, im_height, im_width = im_data.shape
        else:
            im_bands, (im_height, im_width) = 1, im_data.shape
            # 创建文件 create file
        driver = gdal.GetDriverByName("GTiff")  # 数据类型必须有，因为要计算需要多大内存空间 data type
        dataset = driver.Create(filename, im_width, im_height, im_bands, datatype)

        dataset.SetGeoTransform((origin_x, pixel_width, 0, origin_y, 0, pixel_height))  # 写入仿射变换参数
        dataset.SetProjection(im_proj)  # 写入投影
        print('File name: ', filename, ' and Bands Numbers:', im_bands)

        if im_bands == 1:
            dataset.GetRasterBand(1).WriteArray(im_data)  # 写入数组数据
        else:
            for i in range(im_bands):
                dataset.GetRasterBand(i + 1).WriteArray(im_data[i])
                # print('-----------------------------------------')
        del dataset

# 计算某行列下像元经纬度
# def calcLonLat(dataset, x, y):
#     minx, xres, xskew, maxy, yskew, yres = dataset.GetGeoTransform()
#     lon = minx + xres * x
#     lat = maxy +xres * y
#     return lon, lat

def ClipMydatasetTif(file_name, RepetitionRate, outputPath, size):
    #file_name = r"D:\pythorch\data\imagelabel\label.tif"
    RepetitionRate = int(1 - RepetitionRate)
    dataset = gdal.Open(file_name)
    minx, xres, xskew, maxy, yskew, yres = dataset.GetGeoTransform()
    proj, geotrans, data = ClipImageByLocation().read_img(file_name)  # 读数据
    # print(proj)
    # print(geotrans)
    # print(data.shape)
    # print(len(data.shape))
    if (len(data.shape) > 2):
        width = data.shape[1]
        height = data.shape[2]
    else:
        width, height = data.shape
    for j in range(int((height - size * RepetitionRate) / (size * (1 - RepetitionRate)))):
        for i in range(int((width - size * RepetitionRate) / (size * (1 - RepetitionRate)))):
    # for j in range(height // size):  # 切割成256*256小图
    #     for i in range(width // size):
            if (j == height // size):
                # cur_image = data[i * size:(i + 1) * size, j * size:(j + 1) * size]
                if (len(data.shape) == 2):
                    cur_image = data[
                                i * size * (1 - RepetitionRate): (i + 1) * size * (1 - RepetitionRate),
                                j * size * (1 - RepetitionRate): (j + 1) * size * (1 - RepetitionRate)]
                #  如果图像是多波段
                else:
                    cur_image = data[:,
                                i * size * (1 - RepetitionRate): (i + 1) * size * (1 - RepetitionRate),
                                j * size * (1 - RepetitionRate): (j + 1) * size * (1 - RepetitionRate)]
                lon = minx + xres * size * j
                lat = maxy + yres * (i * size)
                ClipImageByLocation().write_img(outputPath.format(i+65, j), proj,
                                                lon, lat, xres, yres, cur_image)  ##写数据
            else:
                # cur_image = data[i*size:(i + 1) * size, j * size:(j + 1) * size]
                if (len(data.shape) == 2):
                    cur_image = data[
                                i * size * (1 - RepetitionRate): (i + 1) * size * (1 - RepetitionRate),
                                j * size * (1 - RepetitionRate): (j + 1) * size * (1 - RepetitionRate)]
                #  如果图像是多波段
                else:
                    cur_image = data[:,
                                i * size * (1 - RepetitionRate): (i + 1) * size * (1 - RepetitionRate),
                                j * size * (1 - RepetitionRate): (j + 1) * size * (1 - RepetitionRate)]

                lon = minx + xres * size * j
                lat = maxy + yres * (i * size)
            ClipImageByLocation().write_img(outputPath.format(i+65, j), proj,
                                                lon, lat, xres, yres, cur_image)  ##写数据

if __name__ == "__main__":
    # os.chdir(r'E:/data')  # 切换路径到待处理图像所在文件夹
    #滑动窗口裁剪函数
    #ClipMydatasetTif('影像路径','重复率','输出路径和名字命名',裁切大小)

    ClipMydatasetTif(r"D:\2020SentinelData\GFDATA\FeatureSelTif\FSTifStretch_new\GF6_20190403_2.tif", 0.1,
                     r'D:\2020SentinelData\GF_9bands_trainingdata\image\{}_{}.tif', 256)

    ClipMydatasetTif(r"D:\2020SentinelData\GFDATA\MaksTif\GF6_area2_20190403_DIS.tif", 0.1,
                     r'D:\2020SentinelData\GF_9bands_trainingdata\label\{}_{}.tif', 256)

    # My data sets including Sentinel-2A and Gaofen PMS
    # GF 9-bands imagepath  D:\2020SentinelData\GFDATA\FeatureSelTif\FSTifStrecth
    # image GF1_20200318_1277_1.tif  GF1_20200318_1277_2.tif  GF6_20190403_1.tif  GF6_20190403_2.tif
    # labelpath D:\2020SentinelData\GFDATA\Mask\prediction_mask
    # label  GF1_1277_1_mosaiced.tif  GF1_1277_2_mosaiced.tif  GF6_1_mosaiced.tif  GF6_2_mosaiced.tif

    #GF 4-bands imagepath  D:\2020SentinelData\GFDATA\StretchTif
    # image GF1_1277_1_20200318.tif    GF1_1277_2_20200318.tif     GF6_1_20190403.tif       GF6_2_20190403.tif

    #D:\2020SentinelData\FeatureBands\StrecthData
    #20190403T031153_T50SKD_4.tif 20190403T031153_T50SKD_5.tif                              20190403T031153_T50SKD_6_clip.tif
    #20200417T030544_T50SKD_5.tif 20200417T030544_T50SKD_6_clip.tif                         20200417T030544_T50SKD_4.tif
    #20200417T030544_T50SKE_1_clip.tif 20200417T030544_T50SKE_2.tif 20200417T030544_T50SKE_3.tif


    #D:\2020SentinelData\mask\MaskResultTIF20210425
    #20190403T50SKD4_dis600_DIS.tif    20190403T50SKD5_dis600_DIS.tif
    #20200417T50SKD5_dis600_DIS.tif    20200417T50SKD6_dis600_DIS.tif
    #20200417T50SKE1_dis600_DIS.tif    20200417T50SKE2_dis600_DIS.tif    20200417T50SKE3_dis600_DIS.tif


    #D:\2020SentinelData\bands\StrecthDataTIFF
    #20190403T031153_T50SKD_4.tif    20190403T031153_T50SKD_5.tif                              20190403T031153_T50SKD_6_clip.tif
    #20200417T030544_T50SKD_5.tif    20200417T030544_T50SKD_6_clip.tif                         20200417T030544_T50SKD_4.tif
    #20200417T030544_T50SKE_1_clip.tif    20200417T030544_T50SKE_2.tif    20200417T030544_T50SKE_3.tif

    #D:\2020SentinelData\mask\MaskResultTIF20210425
    #20190403T50SKD4_dis600_DIS.tif 20190403T50SKD5_dis600_DIS.tif
    #20200417T50SKD5_dis600_DIS.tif 20200417T50SKD6_dis600_DIS.tif
    #20200417T50SKE1_dis600_DIS.tif 20200417T50SKE2_dis600_DIS.tif 20200417T50SKE3_dis600_DIS.tif

    # ClipMydatasetTif(r"D:\2020SentinelData\StrecthDataTIFF\20200417T50SKE1.tif", 0.1, r'D:\2020SentinelData\Process\test\{}_{}.tif', 64)
    # ClipMydatasetTif(r"D:\2020SentinelData\MaskTIF\20200417T50SKE3Mask.tif", 0.1, r'D:\2020SentinelData\Process\label\{}_{}.tif', 64)
    print('------------------------Success-------------------')

