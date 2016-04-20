__author__ = 'akashkakumani'
import RandomizedResponse as rr
import ConvertFile as cf
from scipy.spatial import distance
import numpy as np


def RecoverDistanceRR(p,X):
    (n,k) = X.shape
    dist = []
    for i in range(0,n):
        row = []
        for j in range(0, n):
            if (i == j):
                row.append(0)
            else:
                row.append("{} compared with {}".format(i,j))
                userA = X[i]
                userB = X[j]
                euc = distance.euclidean(userA, userB)**2
                tmp = (euc - (2*k*p)*(1-p))/((1-2*p)**2)
                row.append(tmp)
        dist.append(row)
    return np.array(dist)

output1 = rr.RandomizedResponse(0.4,cf.getHeart())
print(RecoverDistanceRR(0.4,output1))