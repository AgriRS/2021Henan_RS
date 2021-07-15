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

def test(model_path, output_dir, test_loader, addNDVI):
    in_channels = 10
    if(addNDVI):
        in_channels += 1

    model = smp.UnetPlusPlus(
            encoder_name="resnet101e",
            encoder_weights="imagenet",
            in_channels=in_channels,
            classes=8,
    )
    if("swa" in model_path):
        model = AveragedModel(model)
    model.to(DEVICE);
    model.load_state_dict(torch.load(model_path))
    model.eval()

    for image, image_stretch, image_path, ndvi in test_loader:
        with torch.no_grad():
            image = image.cuda()
            image_stretch = image_stretch.cuda()
            output1 = model(image).cpu().data.numpy()
            output2 = model(image_stretch).cpu().data.numpy()
        output = (output1 + output2) / 2.0
        for i in range(output.shape[0]):
            pred = output[i]
            pred = np.argmax(pred, axis = 0) + 1
            pred = np.uint8(pred)
            save_path = os.path.join(output_dir, image_path[i].replace('.tif', '.png'))
            print(save_path)
            cv2.imwrite(save_path, pred)
        
if __name__ == "__main__":
    start_time = time.time()
    model_path_resnest = "../user_data/model_data/unetplusplus_resnest_upsample_lsce_dc_loss.pth"
    output_dir = '../prediction_result'  
    test_image_paths = glob.glob('../tcdata/Sentinel2A_15bands_256_128model/*.tif')
    addNDVI = False
    batch_size = 16
    num_workers = 8
    test_loader = get_dataloader(test_image_paths, None, "test", addNDVI, batch_size, False, 8)
    test(model_path_resnest, output_dir, test_loader, addNDVI)
    print((time.time()-start_time)/60**1)
