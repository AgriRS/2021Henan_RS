# -*- coding: utf-8 -*-
import glob
from dataProcess import get_dataloader
import torch
import cv2
import numpy as np
import os
import segmentation_models_pytorch as smp
from torch.optim.swa_utils import AveragedModel
import time

DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu' 

def test(model_path_resnest, output_dir, test_loader, addNDVI):
    in_channels = 9
    if(addNDVI):
        in_channels += 1
    model_resnest = smp.UnetPlusPlus(
        encoder_name="timm-regnety_320", #timm-resnest101e
        encoder_weights="imagenet",
        in_channels=in_channels,
        classes=8,
        )

    if("swa" in model_path_resnest):
        model_resnest = AveragedModel(model_resnest)
    model_resnest.to(DEVICE);
    model_resnest.load_state_dict(torch.load(model_path_resnest))
    model_resnest.eval()
    for image, image_stretch, image_path, ndvi in test_loader:
        with torch.no_grad():
            image_flip2 = torch.flip(image,[2])
            image_flip2 = image_flip2.cuda()
            image_flip3 = torch.flip(image,[3])
            image_flip3 = image_flip3.cuda()
            image = image.cuda()
            image_stretch = image_stretch.cuda()
            
            output1 = model_resnest(image).cpu().data.numpy()
            output2 = model_resnest(image_stretch).cpu().data.numpy()
            
            output5 = torch.flip(model_resnest(image_flip2),[2]).cpu().data.numpy()
            output7 = torch.flip(model_resnest(image_flip3),[3]).cpu().data.numpy()
        output = (output1 + output2 + output5 + output7) / 4.0
        for i in range(output.shape[0]):
            pred = output[i]
            pred = np.argmax(pred, axis = 0) + 1
            pred = np.uint8(pred)
            save_path = os.path.join(output_dir, image_path[i].split('\\')[-1].replace('.tif', '.png'))
            print(save_path)
            cv2.imwrite(save_path, pred)

if __name__ == "__main__":
    start_time = time.time()
    model_path_resnest = r"../user_data/model_data/unetplusplus_resnest119_1_upsample_SoftCE_dice.pth"
    test_image_paths = glob.glob(r'G:/DLdatasets/Unet_resnet/GF_9_traing_prediction/Gaofen_9bands_256_118model/*.tif')
    addNDVI = False
    batch_size = 16
    num_workers = 8
    test_loader = get_dataloader(test_image_paths, None, "test", addNDVI, batch_size, False, 8)
    test(model_path_resnest, output_dir, test_loader, addNDVI)
    print((time.time()-start_time)/60**1)
