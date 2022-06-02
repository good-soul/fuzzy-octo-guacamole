# Uses image from file for testing
#
# Run as "python step_10_staticImage_v3_Test.py 4_grayscale.png"
# or
# Run as "python step_10_staticImage_v3_Test.py 5_resize.png"
#

import os
import sys
import cv2
import numpy as np
import onnxruntime as ort

filename = sys.argv[1]

index_to_letter = list('ABCDEFGHIKLMNOPQRSTUVWXY')
mean = 0.485 * 255.
std = 0.229 * 255.

# create runnable session with exported model
ort_session = ort.InferenceSession("signlanguage.onnx")

# my_img_4 = cv2.imread('4_grayscale.png', 0)
# my_img_5 = cv2.imread('5_resize.png', 0)

my_img = cv2.imread(filename, 0)

x = cv2.resize(my_img, (28, 28))
x = x.reshape(1, 1, 28, 28).astype(np.float32)
y = ort_session.run(None, {'input': x})[0]
index = np.argmax(y, axis=1)
letter = index_to_letter[int(index)]

print(letter)