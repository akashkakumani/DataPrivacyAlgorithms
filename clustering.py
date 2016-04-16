from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import getDistance as gd

'''
X = gd.studentMatrix()
kmeans = KMeans(init='k-means++',n_clusters = 2, n_init=20)
y_pred = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
error = kmeans.inertia_

colors = np.array([x for x in ('bgrcmyk')])
colors = np.hstack([colors] * 20)

plt.scatter(X[:, 0], X[:, 1], color=colors[y_pred].tolist())

print "KMeans++ Error ", error #Sum of distances of samples to their closest cluster center
plt.show()
'''

#for original student distance matrix
X = gd.studentMatrix()
Z = linkage(X, 'ward')
print X.shape
c, coph_dists = cophenet(Z, pdist(X))
print "Hierarchical Error ",(1.0 - c) #Closer to 1, the better the fit

plt.title('Hierarchical Clustering Dendrogram on original distance matrix(truncated)')
plt.xlabel('cluster size')
plt.ylabel('distance')

#truncated dendrogram
dendrogram(
    Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=12,  # show only the last p merged clusters
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()

#for dp student distance matrix
X = gd.privateStudent()
print X.shape
Z = linkage(X, 'ward')
c, coph_dists = cophenet(Z, pdist(X))
print "Hierarchical Error ",(1.0 - c) #Closer to 1, the better the fit

plt.title('Hierarchical Clustering Dendrogram on DP distance matrix(truncated)')
plt.xlabel('cluster size')
plt.ylabel('distance')

#truncated dendrogram
dendrogram(
    Z,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=12,  # show only the last p merged clusters
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()
