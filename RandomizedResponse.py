__author__ = 'akashkakumani'

import numpy as np
import random

def inputMatrix(rows,columns):
    return np.random.randint(2,size=(rows,columns))




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


