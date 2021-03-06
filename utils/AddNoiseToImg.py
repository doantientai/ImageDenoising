
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import math
import os

from os import listdir
from os.path import isfile, join

from PIL import Image

gau_sigma = 50

path_img_root = '/home/student/tai/m2/Data/'
namedir_img_orig = 'resize_256/'
namedir_img_noise = namedir_img_orig[0:len(namedir_img_orig)-1] + '_gaus' + str(gau_sigma) + '/'
path_img_org = path_img_root + namedir_img_orig
path_img_noise = path_img_root + namedir_img_noise

# print(namedir_img_noise)

### make noisy dir if not exist
if not os.path.exists(path_img_noise):
    os.makedirs(path_img_noise)

def add_gauss_noise_gray(image, sigma):
    image_amax = (np.amax(image)).astype(float) # because some image 0..1, some some others 0..255
    row,col= image.shape
    mean = 0
    sigma = sigma/(255.0/image_amax)
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)    
    noisy = image + gauss
    noisy_clipped = np.clip(noisy, 0.0, image_amax)
    return noisy_clipped

def mse2(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(np.size(imageA))
	return err

def psnr(im1,im2, pmax=1.0):
    NUM_ELEMENTS = np.size(im1)   
    mse = mse2(im1, im2) 
    psnr = 10*np.log10(pmax**2/mse)
    return psnr

def saveImgWithPIL(img, path):
    ### input is an array range 0.0 to 1.1
    img *= 255.0/img.max()
    img = np.uint8(img)
    img_pil = Image.fromarray(img)
    img_pil.save(path)

### list original images
list_img_org = [f for f in listdir(path_img_org) 
                if isfile(join(path_img_org, f))]
print('number of images:', len(list_img_org))

### add noise to each image
count = 0
list_img_len = len(list_img_org)
for img_name in list_img_org:
    img = np.array(Image.open(path_img_org + img_name))
#     print('amax:', (np.amax(img)).astype(float))
    
    img_n = add_gauss_noise_gray(img, gau_sigma)
#     print('amax img_n:', np.amax(img_n))
#     saveImgWithPIL(img_n, path_img_noise + img_name)
    count += 1
    if count % 10 == 0:
        print('Adding noise: ', count, '/', list_img_len, end='\r')
print('',end='\n')
print('DONE!')
