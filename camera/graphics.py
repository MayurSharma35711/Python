import numpy as np
import cv2 as cam
import time
import camera
import engine
import math
# import curses

for i in range(0,10):
    print("2")
    time.sleep(.1)
cam.destroyAllWindows()

size = 30

# HAS TO BE SQUARE FRAME

frameX = np.zeros((size, size))
frameX[10:20, 10:20] = np.ones((10, 10))
frameY = np.zeros((size, size))
frameY[10:20, 10:20] = np.ones((10, 10))
frameZ = np.zeros((size, size))
for i in range(1, 10):
    frameZ[20-i, 10:(10+i)] = 1

phi = 0  # y and height angle
theta = 0  # xz angle
# screen = curses.initscr()
# curses.cbreak()
# screen.keypad(True)

physicalFrame = np.zeros((size,size,size))
physicalFrame = engine.create3D(physicalFrame,frameX,frameY,frameZ)
multi_frame = np.zeros((size,size))
multi_frame = camera.resize(multi_frame,10)
ddangleFactor = math.pi / 180


def emulator(ang1,ang2):
    ang1 = math.radians(ang1)
    ang2 = math.radians(ang2)
    x = math.cos(ang1)
    z = math.sin(ang1)
    y = math.cos(ang2)
    base = math.sqrt(x ** 2 + z ** 2)
    height = math.sqrt(x * z + y ** 2)
    area = base * height / 2
    alpha = size ** 2 / (4 * area)
    frame_counter = np.array([round(x,3), round(y,3), round(z,3)])
    frame_back = np.array([alpha*x, alpha*y, alpha*z])
    return frame_counter, frame_back
# this works, it's just really slow, so maybe actually write it in C and get the array from python
# do all image processing in python, do all creating in C/C++, so this graphics file should be in C
# work on getting camera and contours working


# this might need to optimized
# something like it returns an array for C code to run
# while True:
#     count, back = emulator(theta, phi)
#     # now basically take the background frame, and create a cut-out section from the 3D frame using the counter
#     # iterate through and get each of those column like things
#     # then take that and use the maximum of those terms to get what you will actually display
#     # so give this array into SFML and have it actually display stuff
#     cam.imshow('3D', multi_frame)
#     print(count)
#     if cam.waitKey(1) & 0xFF == ord('e'):
#         print("exit")
#         break
#     if cam.waitKey(1) & 0xFF == ord('w'):
#         phi += 5
#     elif cam.waitKey(1) & 0xFF == ord('s'):
#         phi -= 5
#     elif cam.waitKey(1) & 0xFF == ord('d'):
#         theta += 5
#     elif cam.waitKey(1) & 0xFF == ord('a'):
#         theta -= 5

