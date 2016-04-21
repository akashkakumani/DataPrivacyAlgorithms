__author__ = 'akashkakumani'
import PrivateProtection as pp
import RandomizedResponse as rr
import ConvertFile as cf
import numpy as np
import math
from scipy.spatial import distance


'''
def heartCombined():
    output1 = rr.Rotate(cf.getHeart())
    Zheart, Pheart = pp.PrivateProtection(cf.getHeart())
    Zcombined1, P = pp.PrivateProtection(output1)
    return Zcombined1


def studentCombined():
    output2 = rr.RandomizedResponse(0.4,cf.getStudent())
    Zstudent, Pstudent = pp.PrivateProtection(cf.getStudent())
    Zcombined2, P = pp.PrivateProtection(output2)
    return Zcombined2
'''


def studentPP():
    output = cf.getStudent()
    Zstudent, Pstudent, sigma = pp.PrivateProtection(output)
    distance = pp.recoveredDistance(Zstudent,sigma)
    return distance

def studentRR():
    output = cf.getStudent()
    #privacy parameter
    p = .1
    Xstudent = rr.RandomizedResponse(p, output)
    distance = rr.RecoverDistanceRR(p,Xstudent)
    return distance


def printResults():
    print ("******************************************************************************")
    print ("******************************  RANDOMIZED RESPONSE  *************************")
    print ("******************************************************************************\n")


    print("INPUT RANDOMIZED RESPONSE + HEART TEXT: \n\n {} \n".format(cf.getHeart()))
    output1 = rr.RandomizedResponse(0.4,cf.getHeart())
    print("OUTPUT RANDOMIZED RESPONSE + HEART TEXT: \n\n {} \n".format(output1))

    print("INPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n\n {} \n".format(cf.getStudent()))
    output2 = rr.RandomizedResponse(0.4,cf.getStudent())
    print("OUTPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n\n {} \n".format(output2))



    print ("******************************************************************************")
    print ("******************************   PRIVATE PROTECTION   *************************")
    print ("******************************************************************************\n")

    print("INPUT PRIVATE PROTECTION + HEART TEXT: \n\n {} \n".format(cf.getHeart()))
    Zheart, Pheart, sigma = pp.PrivateProtection(cf.getHeart())
    print("OUTPUT PRIVATE PROTECTION Z + HEART TEXT: \n\n {} \n".format(Zheart))
    print("OUTPUT PRIVATE PROTECTION P + HEART TEXT: \n\n {} \n".format(Pheart))


    print("INPUT PRIVATE PROTECTION + STUDENT TEXT: \n\n {} \n".format(cf.getStudent()))
    Zstudent, Pstudent, sigma = pp.PrivateProtection(cf.getStudent())
    print("OUTPUT PRIVATE PROTECTION Z + STUDENT TEXT: \n\n {} \n".format(Zstudent))
    print("OUTPUT PRIVATE PROTECTION P + STUDENT TEXT: \n\n {} \n".format(Pstudent))


    print ("*********************************************************************")
    print ("******************************   RECOVERED DISTANCE   *************************")
    print ("*********************************************************************\n")

    print("INPUT PRIVATE PROTECTION + HEART TEXT: \n\n {} \n".format(cf.getHeart()))
    Zheart, Pheart, sigma = pp.PrivateProtection(cf.getHeart())
    print("OUTPUT PRIVATE PROTECTION Z + HEART TEXT: \n\n {} \n".format(Zheart))
    distance = pp.recoveredDistance(Zheart,sigma)


    print(distance[0])
    print(distance[1])
    print(distance[2])
    ##print("OUTPUT RECOVERED DISTANCE Z + HEART TEXT: \n\n {} \n".format(distance))
