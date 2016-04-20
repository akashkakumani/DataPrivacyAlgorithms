__author__ = 'akashkakumani'
import random
import numpy as np
import math
from scipy.spatial import distance

def generateP(d, k):
    Matrix = np.array([[float(0) for x in range(k)] for x in range(d)])
    count = 0
    for c in range(0,k):
        for r in range(0,d):
            s = random.random() * 6
            cell = -1
            if s < 1:
                cell = pow(float(3)/k,.5)
            elif s < 5:
                cell = 0
                count+=1
            else:
                cell = pow(float(3)/k,.5)
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

def generateNoiseMatrix(delta,epsilon,Y,P):
    logInput = float(1)/(2*delta)
    ln = math.log(logInput,math.e) + epsilon
    W = generateW(2,P)
    sigma = W * (math.sqrt((2*ln))/epsilon)

    rows, col = Y.shape
    s = np.random.normal(0, sigma**2, rows*col)
    noiseMatrix = np.array([[float(0) for x in range(col)] for x in range(rows)])
    count = 0
    for c in range(0,col):
        for r in range(0,rows):
            noiseMatrix[r][c] = s[count]
            count+=1
    return noiseMatrix,sigma




def PrivateProtection(input):
    (n,d) = input.shape


    k = 40 # WE DONT KNOW WHAT THIS VALUE SHOULD BE
    P = generateP(d,k)

    x = np.matrix(input)
    p = np.matrix(P)

    Y = x*p

    noise,sigma = generateNoiseMatrix(0.4, 0.1,Y,P)

    Z = np.add(Y,noise)
    return Z,p,sigma


def recoveredDistance(Z, sigma):
    print sigma
    (n,k) = Z.shape
    dist = []
    for i in range(0,n):
        row = []
        for j in range(0, n):
            if (i == j):
                row.append(0)
            else:
                userA = Z[i]
                userB = Z[j]

                y = distance.euclidean(userA, userB)
                if y < 0 or y < 100:
                    print y
                y = y - (2*k*(sigma**2))
                row.append(y)

        dist.append(row)
    return np.array(dist)
