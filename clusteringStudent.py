#GET CLUSTERING FOR STUDENT DATA USING ORIGINAL, PP, AND RR

from sklearn.cluster import KMeans
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
from scipy.spatial.distance import pdist
import getDistance as gd
import GenMatrix as gm

generatedMatrix = gm.cluster(200)

##############
'''ORIGINAL'''
##############

#for original student distance matrix
X = gm.distanceMatrix(generatedMatrix)
Z = linkage(X, 'ward')
c, coph_dists = cophenet(Z, pdist(X))
#print "Hierarchical Error ",(c) #Closer to 0, the better the fit

plt.title('Hierarchical Clustering Dendrogram on Original Distance Matrix')
plt.ylabel('Distance')
plt.xlabel('Leaf Nodes')

#truncated dendrogram
To = dendrogram(
    Z,
    no_labels=True
)

#Get data points in each cluster
labelsOriginal = To['ivl']
clustersOriginal = fcluster(Z,0.7*max(Z[:,2]),'distance')
clustersOriginalDict = defaultdict(list)
colorsOriginal = To['color_list']

for x in range(0, len(colorsOriginal)):
    #clustersOriginalDict[clustersOriginal[x]].append(int(labelsOriginal[x]))
    clustersOriginalDict[colorsOriginal[x]].append(int(labelsOriginal[x]))

for x in clustersOriginalDict.keys():
    clustersOriginalDict[x].sort()

plt.show()

########################
'''PRIVATE PROJECTION'''
########################

#for dp student distance matrix
X = gd.ppGM(generatedMatrix)
Z = linkage(X, 'ward')
c, coph_dists = cophenet(Z, pdist(X))
#print "Hierarchical Error ",(c) #Closer to 0, the better the fit

plt.title('Hierarchical Clustering Dendrogram on PP Distance Matrix')
plt.ylabel('Distance')
plt.xlabel('Leaf Nodes')

#truncated dendrogram
Tpp = dendrogram(
    Z,
    no_labels=True
)

#Get data points in each cluster
labelsPP = Tpp['ivl']
colorsPP = Tpp['color_list']
clustersPP = fcluster(Z,0.7*max(Z[:,2]),'distance')
clustersPPDict = defaultdict(list)

for x in range(0, len(colorsPP)):
    #clustersPPDict[clustersPP[x]].append(int(labelsPP[x]))
    clustersPPDict[colorsPP[x]].append(int(labelsPP[x]))

for x in clustersPPDict.keys():
    clustersPPDict[x].sort()

#Get percentage of data points that are in the same clusters:
for x in clustersOriginalDict.keys():
    maximum = 0
    for y in clustersPPDict.keys():
        l1 = np.array(clustersOriginalDict[x])
        l2 = np.array(clustersPPDict[y])
        d = [val for val in l1 if val in l2]
        percent = (len(d)*1.0)/(len(l1)*1.0)
        #Take highest percentage overlap for each cluster in original
        if percent > maximum:
            maximum = percent
            comp1 = x
            comp2 = y
    if comp1 != 'b':
        print "Original vs PP ", comp1, comp2, maximum
print
'''
#Get percentage of data points that are in the same cluster in both:
differencePP = np.array(sclustersOriginal) - np.array(sclustersPP)

count = 0
for x in list(differencePP):
    if x == 0:
        count+=1

percentDifferencePP = 1.0 - (count*1.0)/(len(differencePP)*1.0)
'''

plt.show()

##########################
'''RANDOMIZED RESPONSE'''
##########################

#for dp student distance matrix
X = gd.rrGM(generatedMatrix)
#print X.shape
Z = linkage(X, 'ward')
c, coph_dists = cophenet(Z, pdist(X))
#print "Hierarchical Error ",(c) #Closer to 0, the better the fit

plt.title('Hierarchical Clustering Dendrogram on RR Distance Matrix')
plt.ylabel('Distance')
plt.xlabel('Leaf Nodes')

#truncated dendrogram
Trr = dendrogram(
    Z,
    no_labels=True
)

#Get data points in each cluster
labelsRR = Trr['ivl']
clustersRR = fcluster(Z,0.7*max(Z[:,2]),'distance')
clustersRRDict = defaultdict(list)
colorsRR = Trr['color_list']

for x in range(0, len(colorsRR)):
    #clustersRRDict[clustersRR[x]].append(int(labelsRR[x]))
    clustersRRDict[colorsRR[x]].append(int(labelsRR[x]))

for x in clustersRRDict.keys():
    clustersRRDict[x].sort()

#Get percentage of data points that are in the same cluster in both:
for x in clustersOriginalDict.keys():
    maximum = 0
    for y in clustersRRDict.keys():
        l1 = np.array(clustersOriginalDict[x])
        l2 = np.array(clustersRRDict[y])
        d = [val for val in l1 if val in l2]
        percent = (len(d)*1.0)/(len(l1)*1.0)
        #Take highest percentage overlap for each cluster in original
        if percent > maximum:
            maximum = percent
            comp1 = x
            comp2 = y
    if comp1 != 'b':
        print "Original vs RR ", comp1, comp2, maximum

'''
#Get percentage of data points that are in the same cluster in both:
differenceRR = np.array(sclustersOriginal) - np.array(sclustersRR)

count = 0
for x in differenceRR:
    if x == 0:
        count+=1

percentDifferenceRR = 1.0 - (count*1.0)/(len(differenceRR)*1.0)
'''
plt.show()
