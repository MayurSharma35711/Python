import cv2 as cam
import numpy as np
import time
import engine

for i in range(0,10):
    print("1")
    time.sleep(.1)

def resizer(img,factor):
    h = int(img.shape[1] * factor)
    w = int(img.shape[0] * factor)
    img = cam.resize(img, (h, w))
    return img


x = cam.imread("/Users/mayur/Documents/Data/drive-download-20190430T145927Z-001/IMG_2449.JPG")
y = cam.imread("/Users/mayur/Documents/Data/drive-download-20190430T145927Z-001/IMG_2450.JPG")
z = cam.imread("/Users/mayur/Documents/Data/drive-download-20190430T145927Z-001/IMG_2451.JPG")

xwin = 'xf'
ywin = 'yf'
zwin = 'zf'

# print(x.shape)
x = resizer(x, .1)
y = resizer(y, .1)
z = resizer(z, .1)
cam.imshow(xwin, x)
cam.imshow(ywin, y)
cam.imshow(zwin, z)
cam.waitKey(0)

full = engine.create3D(x, y, z)
cam.imshow('start', full[0])
cam.imshow('mid', full[99])
cam.imshow('end', full[199])

cam.destroyAllWindows()
print("done")

# get contours here and pass into engine functions
