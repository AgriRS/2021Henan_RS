from osgeo import gdal

# !----------  After stretch to 0-255 in ENVI，
# If the coordinate system is lost, the original image coordinate system
# is added to the processed image to keep the spatial position correct
# 会出现坐标系丢失，将原图像坐标系加入处理后的图像，保持空间位置正确性 ---------------！#

def addcoor(img1, img2): #img1为有坐标系，img2为无坐标系 img1 is the original image coordinate system,img2 is the stretch image
    dataset1 = gdal.Open(img1)
    geotrans = dataset1.GetGeoTransform()
    proj = dataset1.GetProjection()
    dataset2 = gdal.Open(img2, 1)
    dataset2.SetGeoTransform(geotrans)
    dataset2.SetProjection(proj)
    del dataset1
    del dataset2

if __name__=='__main__':

    addcoor(r'D:\pythorch\data\imagelabel\image.tif', r'D:\pythorch\data\imagelabel\strecth\image.tif')