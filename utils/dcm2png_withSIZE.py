import dicom
import os
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline

# import scipy.io
from cv2 import imwrite
from cv2 import resize
import cv2

EXPECTED_SIZE = 256

PathDicom = '/users/taitien.doan/CTLymphNodes/DOI/'
PathPng = '/home/tai-databases/CTLymphNodes/PNG/resize_' + str(EXPECTED_SIZE) + '/'
### make PathPng dir if not exist
if not os.path.exists(PathPng):
    os.makedirs(PathPng)
    
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))
            

count_process = 0
count_finish = len(lstFilesDCM)
for file in lstFilesDCM:
    RefDs = dicom.read_file(file)
    name_output = file[99:104]+ '_' + file[len(file)-10:len(file)-3]+'png'
    img = RefDs.pixel_array
    img = img / img.max() * 255.0
    img_resized = resize(img, (EXPECTED_SIZE,EXPECTED_SIZE))
    imwrite(PathPng + name_output, img_resized)
#     print("writing to ", PathPng + name_output)
    count_process += 1
    if (count_process % 100 == 0):
        print('Progress:', count_process, '/', count_finish , end='\r')
print('DONE!')
