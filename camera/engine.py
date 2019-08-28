import numpy as np
import cv2 as cam
import time

sizeX = 30
sizeY = 30
sizeZ = 30

frameX = np.zeros((sizeX, sizeY))
frameX[10:20, 10:20] = np.ones((10, 10))
frameY = np.zeros((sizeZ, sizeY))
frameY[10:20, 10:20] = np.ones((10, 10))
frameZ = np.zeros((sizeZ, sizeX))
# for i in range(1,10):
#     frameZ[20-i,10:(10+i)] = 1

# direction: 0 means image from front, 1 means image from right rel front, 2 means image from top rel front
# defines front face
def combineX(x, original):
    for k in range(0, x.shape[0]):
        original[:][:][k] = x
        return original

# defines right face
def combineY(y,original):
    for i in range(0, original.shape[2]):
        cam.bitwise_and(original[i], y, original[i])
    return original

# defines top view from right
def combineZ(z,original):
    for i in range(0, z.shape[0]):
        cam.bitwise_and(original[:][i][:], z, original[:][i][:])
    return original

# def fix_col(original, i, k, j):
#     if original[i][k][j] is 1:
#         original[i][k][j] = x[i][j] + y[j][i]

# dstack

def print3D(frame):
    print("prints xy cross-sections")
    for i in range(0, frame.shape[0]):
        for j in range(0, frame.shape[1]):
            for k in range(0, frame.shape[2]):
                print(int(frame[i][j][k]), end="")
            print("\t")
        print("\n")

def create3D(X, Y, Z):
    phy = np.zeros((X.shape[0], Y.shape[1], Z.shape[0]))
    phy = combineX(X, phy)
    phy = combineY(Y, phy)
    phy = combineZ(Z, phy)
    return phy


physicalFrame = create3D(frameX, frameY, frameZ)
print3D(physicalFrame)


# while (True):
#    cam.imshow('x', frameX)
#    cam.imshow('y', frameY)
#    if cam.waitKey(1) & 0xFF == ord('e'):
#        print("exit")
#        break
# cam.destroyAllWindows()
print("done")
