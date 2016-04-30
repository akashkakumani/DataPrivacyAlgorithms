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
    for i in range (0,n/4):
        a.append(1)
    for i in range(n/4,n):
        a.append(0)
    cluster1.append(a)


    cluster2 = []
    b = []
    for i in range (0,n/4):
        b.append(0)
    for i in range(n/4,n - n/2):
        b.append(1)
    for i in range(n - n/2, n):
        b.append(0)
    cluster2.append(b)


    cluster3 = []
    c = []
    for i in range(0,n - n/2):
        c.append(0)
    for i in range(n - n/2, n - n/4):
        c.append(1)
    for i in range(n - n/4, n):
        c.append(0)
    cluster3.append(c)


    cluster4 = []
    d = []
    for i in range(0,n - n/4):
        d.append(0)
    for i in range(n - n/4, n):
        d.append(1)
    cluster4.append(d)


    for j in range(0,300):
        c1 = []
        c2 = []
        c3 = []
        c4 = []
        for i in range(0,len(a)):
            r = random.random()
            if r > 0.10:
                c1.append(a[i])
                c2.append(b[i])
                c3.append(c[i])
                c4.append(d[i])
            else:
                c1.append( 1 - a[i])
                c2.append( 1 - b[i])
                c3.append( 1 - c[i])
                c4.append( 1 - d[i])
        cluster1.append(c1)
        cluster2.append(c2)
        cluster3.append(c3)
        cluster4.append(c4)

    return np.array(cluster1 + cluster2 + cluster3 + cluster4)


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
