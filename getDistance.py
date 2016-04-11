import ConvertFile as cf
from scipy.spatial import distance

def studentMatrix():
    matrix = cf.getStudent()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist

def heartMatrix():
    matrix = cf.getHeart()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist
