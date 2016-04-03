__author__ = 'akashkakumani'
import random
import numpy as np
import math

def randomMatrix(rows, columns):
    Matrix = np.array([[float(0) for x in range(columns)] for x in range(rows)])
    count = 0
    for c in range(0,columns):
        for r in range(0,rows):
            s = random.random() * 6
            cell = -1
            if s < 1:
                cell = pow(float(3)/columns,.5)
            elif s < 5:
                cell = 0
                count+=1
            else:
                cell = pow(float(3)/columns,.5)
                cell *= -1
            Matrix[r][c] = cell
    return Matrix


def inputMatrix(rows,columns):
    return np.random.randint(2,size=(rows,columns))

def generateW(rho,P):
    rows, col = P.shape
    maxSum = 0
    for i in range(0,rows):
        sum = 0
        for j in range(0,col):
            sum += (abs(P[i][j])**rho)
        sum**(1.0/rho)
        if sum > maxSum:
            maxSum = sum
    return maxSum

def generateNoiseMatrix(delta,epsilon,P):
    logInput = float(1)/(2*delta)
    ln = math.log(logInput,math.e) + epsilon
    W = generateW(2,P)
    sigma = W * (math.sqrt((2*ln))/epsilon)
    rows, col = P.shape
    s = np.random.normal(0, sigma**2, rows*col)
    noiseMatrix = np.array([[float(0) for x in range(col)] for x in range(rows)])
    count = 0
    for c in range(0,col):
        for r in range(0,rows):
            noiseMatrix[r][c] = s[count]
            count+=1
    return noiseMatrix

def multRandomWithInput(input):
    m1 = input
    rows, col = m1.shape
    m2 = randomMatrix(rows, col)
    return np.multiply(m1,m2)


def PrivateProtection():
    input = inputMatrix(5,5)
    #print("INPUT :\n {} \n".format(input))
    noise = generateNoiseMatrix(0.4, 0.1,input)
    #print("NOISE :\n {} \n".format(noise))
    mult = multRandomWithInput(input)
    #print("MULT :\n {} \n".format(mult))
    finalProduct = np.add(noise,mult)
    return finalProduct,mult

Z,P = PrivateProtection()
print("PUBLISHING P :\n {} \n".format(P))
print("PUBLISHING Z :\n {} \n".format(Z))