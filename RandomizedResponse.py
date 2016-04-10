__author__ = 'akashkakumani'

import numpy as np
import random

def inputMatrix(rows,columns):
    return np.random.randint(2,size=(rows,columns))


def Rotate(pixels):

    print("INPUT :\n {} \n".format(pixels))

    MAXROW = len(pixels)
    MAXCOL = len(pixels[0])
    m = np.array([[float(0) for x in range(MAXROW)] for x in range(MAXCOL)])
    for r in range(MAXROW):
        for c in range(MAXCOL):
            m[MAXCOL-1-c][r] = pixels[r][c]
    return m




def RandomizedResponse(p,X):
    rows, col = X.shape
    count = 0
    for j in range(0,col):
        for i in range(0,rows):
            rand = random.random()
            if rand < p:
                count+=1
                X[i][j] = 1 - X[i][j]
    print count
    return X


