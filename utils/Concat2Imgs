import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import math
import os

from os import listdir
from os.path import isfile, join

from PIL import Image

from random import shuffle

SIZE_IMG = 256

### paths to 2 dirs ORIGINAL and NOISY
path_imgs_A = '/home/tai-databases/CTLymphNodes/PNG/resize_256_gaus50/'
path_imgs_B = '/home/tai-databases/CTLymphNodes/PNG/resize_256/'
path_imgs_pair = path_imgs_A[0:len(path_imgs_A)-1] + 'paired' + '/'

### make paired dir if not exist
if not os.path.exists(path_imgs_pair):
    os.makedirs(path_imgs_pair)

### make subdirs if not exist    
train_dir = path_imgs_pair + "train/"
test_dir = path_imgs_pair + "test/"
val_dir = path_imgs_pair + "val/"
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
if not os.path.exists(test_dir):
    os.makedirs(test_dir)
if not os.path.exists(val_dir):
    os.makedirs(val_dir)      

### list name
list_img_name = [f for f in listdir(path_imgs_A) if isfile(join(path_imgs_A, f))]
num_of_images = len(list_img_name)
print('number of images:', num_of_images)    
        
# shuffer image order, divide into 3 sets
index_array = np.arange(num_of_images)
index_array_shuf = index_array
np.random.shuffle(index_array_shuf)
index_train_array = index_array_shuf[0:int(num_of_images/2)]
index_test_array = index_array_shuf[int(num_of_images/2): int(num_of_images*0.75)]
index_val_array = index_array_shuf[int(num_of_images*0.75):num_of_images]    
    

### for each image in A, find the same name image in B
for img_id in range(num_of_images):
    img_name = list_img_name[img_id]
    img_A = Image.open(path_imgs_A + img_name)
    img_B = Image.open(path_imgs_B + img_name)
    img_pair = Image.new('L', (SIZE_IMG*2, SIZE_IMG))
    img_pair.paste(img_A, (0,0))
    img_pair.paste(img_B, (SIZE_IMG,0))
    
    ### save to the properly subdir
    if img_id in index_train_array:
        img_pair.save(train_dir + img_name)
    elif img_id in index_test_array:
        img_pair.save(test_dir + img_name)
    elif img_id in index_val_array:
        img_pair.save(val_dir + img_name)
    
    if img_id % 10 == 0:
        print('Paring up: ', img_id, '/', num_of_images, end='\r')
#     plt.imshow(img_pair,cmap='gray')
    
print('ALL DONE!')
