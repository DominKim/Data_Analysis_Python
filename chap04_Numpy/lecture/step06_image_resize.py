'''
step06_image_resize.py

reshape vs resize
 - reshape : 모양 변경
 - resize  : 크기 변경
  ex) image -> 120 x 150 규격화 -> model

image 규격화 : 실습
'''

from glob import glob # file 검색 패턴 사용(문자열 경로, *.jpg)
from PIL import Image # image file read
import numpy as np
import matplotlib.pyplot as plt
import os
os.getcwd()
# 1개 image file open
path = "/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/chap04_Numpy/"
file = path + "images/test1.jpg"

img = Image.open(file)
type(img) # PIL.JpegImagePlugin.JpegImageFile
np.shape(img) # (360, 540, 3) -> (120, 150, 3) -> (h, w, c)
plt.imshow(img)

img_re = img.resize((150,120)) # w, h : 세로 가로 픽셀 바꿔서 입력해야 함
np.shape(img_re) # (120, 150, 3)
plt.imshow(img_re)

# PIL -> numpy
type(img_re) # PIL.Image.Image
img_arr = np.asarray(img)
img_arr.shape # (360, 540, 3)
type(img_arr) # numpy.ndarray
img_arr.resize(120,150,3)

# 여러장의 image resize 함수
def imageResize():
    img_h = 120 # 세로 픽셀
    img_w = 150 # 가로 픽셀

    image_resize = [] # 규격화된 image 저장

    # glob : file
    for file in glob(path + "images/" + "*.jpg"):
        # test1.jpg -> test2.jpg.
        img = Image.open(file) # image file read
        print(np.shape(img)) # img shape

        # PIL -> resize
        img = img.resize((img_w, img_h)) # w, h
        # PIL -> numpy
        img_data = np.asarray(img)

        # resize image save
        image_resize.append(img_data)
        print(file, ":", img_data.shape) # image shape

    # list -> numpy
    return np.array(image_resize)

image_resize = imageResize()
'''
(360, 540, 3)
/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/chap04_Numpy/images/test1.jpg : (120, 150, 3)
(332, 250, 3)
/Users/mac/Desktop/bigdata/Python/4_Python-II/workspace/chap04_Numpy/images/test2.jpg : (120, 150, 3)
'''

image_resize.shape