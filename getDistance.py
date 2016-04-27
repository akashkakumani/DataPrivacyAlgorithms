import ConvertFile as cf
from scipy.spatial import distance
import Main as main
import numpy as np
import PrivateProtection as pp
import GenMatrix as gm
import RandomizedResponse as rr

# original matrix distance
def studentMatrix():
    matrix = cf.getStudent()
    (n,d) = matrix.shape
    dist = []
    for i in range(0,n):
        row = []
        for j in range(0, n):
            if (i == j):
                row.append(0)
            else:
                #row.append("{} compared with {}".format(i,j))
                userA = matrix[i]
                userB = matrix[j]
                euc = distance.euclidean(userA, userB)**2
                #tmp = (euc - (2*k*p)*(1-p))/((1-2*p)**2)
                row.append(euc)
        dist.append(row)
    return np.array(dist)
    #dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    dist
    return dist

# PP, the recovered distance on student
def ppStudent():
    matrix = main.studentPP()
    return matrix


# original vs PP distance
def differencePPStudent():
    x = studentMatrix()
    #print (x[0])
    y = ppStudent()
    #print y[0]
    return y - x


## RR on studend
def rrStudent():
    matrix = main.studentRR()
    return matrix


## original vs RR DISTANCE
def differenceRRStudent():
    x = studentMatrix()
    y = rrStudent()
    return y - x



def ppGM(generateMatrix):
    Z, P, sigma = pp.PrivateProtection(generateMatrix)
    distance = pp.recoveredDistance(Z, sigma)
    return distance

def rrGM(generateMatrix):
    p = .4
    X = rr.RandomizedResponse(p, generateMatrix)
    distance = rr.RecoverDistanceRR(p, X)
    return distance









# original matrix distance
def heartMatrix():
    matrix = cf.getHeart()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist
