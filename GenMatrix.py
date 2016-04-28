import random
import numpy as np
import math
from scipy.spatial import distance
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import getDistance as gd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



def cluster(n):
    cluster1 = []
    a = []
    for i in range (0,n/3):
        a.append(1)
    for i in range(n/3,n):
        a.append(0)

    cluster1.append(a)

    for j in range(0,300):
        x = []
        for i in range(0,len(a)):
            r = random.random()
            if r > 0.10:
                x.append(a[i])
            else:
                x.append( 1 - a[1])
        cluster1.append(x)


    cluster2 = []
    a = []
    for i in range (0,n/3):
        a.append(0)
    for i in range(n/3,n - n/3):
        a.append(1)
    for i in range(n - n/3, n):
        a.append(0)

    cluster2.append(a)

    for j in range(0,300):
        x = []
        for i in range(0,len(a)):
            r = random.random()
            if r > 0.10:
                x.append(a[i])
            else:
                x.append( 1 - a[1])
        cluster2.append(x)


    cluster3 = []
    a = []
    for i in range(0,n - n/3):
        a.append(0)
    for i in range(n - n/3, n):
        a.append(1)

    cluster3.append(a)

    for j in range(0,300):
        x = []
        for i in range(0,len(a)):
            r = random.random()
            if r > 0.10:
                x.append(a[i])
            else:
                x.append( 1 - a[1])
        cluster3.append(x)


    return np.array(cluster1 + cluster2 + cluster3)



def distanceMatrix(a):
    matrix = cluster(100)
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
