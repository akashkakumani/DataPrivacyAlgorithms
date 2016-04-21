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

def ppStudent():
    matrix = main.studentPP()
    return matrix

def rrStudent():
    matrix = main.studentRR()
    return matrix



