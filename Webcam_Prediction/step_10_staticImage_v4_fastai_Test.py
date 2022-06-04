# Uses image from file for testing
#
# Run as "python step_10_staticImage_v4_fastai_Test.py 1_rawinput.png 275 525 700 950"
#

import os
import sys
import cv2
import numpy as np
from fastai.vision import *

filename = sys.argv[1]
x1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y1 = int(sys.argv[4])
y2 = int(sys.argv[5])

#learn_inf = load_learner('export_50_no_tfms/')
learn_inf = load_learner('export_100_tfms/')
# img = open_image('4_grayscale.png')
image = cv2.imread(filename, 0)


# start_point = (700, 275)
# end_point = (950, 525)
#start_point = (y1, x1)
#end_point = (y2, x2)
#color = (0, 0, 0)
#thickness = 2
#image = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imwrite("12_withRectangle.png", image)

# clone = image.copy()

# crop_img = image[275:525, 700:950]
crop_img = image[x1:x2, y1:y2]
crop_img = cv2.resize(crop_img, (50, 50))

cv2.imwrite("public/intermediate.png", crop_img)

img = open_image('public/intermediate.png')


pred_class,pred_idx,outputs = learn_inf.predict(img)

list = ['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '3', '4', '5', '6', '7', '8']
list_abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print (list_abc[int(list[pred_idx])])

#os.remove('intermediate.png')
