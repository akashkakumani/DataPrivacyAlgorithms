import ConvertFile as cf
from scipy.spatial import distance
import Main as main

def studentMatrix():
    matrix = cf.getStudent()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist

def heartMatrix():
    matrix = cf.getHeart()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist

def privateStudent():
    matrix = main.studentCombined()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist

def privateHeart():
    matrix = main.heartCombined()
    dist = distance.squareform(distance.pdist(matrix, metric='euclidean'))
    return dist

