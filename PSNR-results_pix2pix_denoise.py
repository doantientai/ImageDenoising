import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import math
import os

from os import listdir
from os.path import isfile, join

from PIL import Image

PATH_IMG = '/home/tai/Desktop/M2/ResultsFromServer/images/epoch001_fake_B.png'

def mse2(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(np.size(imageA))
	return err

def psnr(im1,im2, pmax=1.0):
    NUM_ELEMENTS = np.size(im1)   
    mse = mse2(im1, im2) 
    psnr = 10*np.log10(pmax**2/mse)
    return psnr

print("PSNR:")

for i in range(112):
    str_index = str(i+1).zfill(3)
#     print(str_index)
    img_org = np.asanyarray(Image.open(PATH_IMG + "epoch" + str_index + "_real_B.png"), dtype=np.uint8)
    img_denois = np.asanyarray(Image.open(PATH_IMG + "epoch" + str_index + "_fake_B.png"), dtype=np.uint8)
    img_nois = np.asanyarray(Image.open(PATH_IMG + "epoch" + str_index + "_real_A.png"), dtype=np.uint8)
#     plt.imshow(img_denois)
    print("Noisy: %.2f -- Denoised: %.2f (dB)" % (psnr(img_org, img_nois,pmax=255.0), psnr(img_org, img_denois, pmax=255.0)))
#     print(np.amax(img_org))
