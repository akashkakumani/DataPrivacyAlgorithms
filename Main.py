__author__ = 'akashkakumani'
import PrivateProtection as pp
import RandomizedResponse as rr
import ConvertFile as cf
import numpy as np





print ("******************************************************************************")
print ("******************************  RANDOMIZED RESPONSE  *************************")
print ("******************************************************************************\n")


print("INPUT RANDOMIZED RESPONSE + HEART TEXT: \n\n {} \n".format(cf.getHeart()))
output1 = rr.Rotate(cf.getHeart())
print("OUTPUT RANDOMIZED RESPONSE + HEART TEXT: \n\n {} \n".format(output1))

print("INPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n\n {} \n".format(cf.getStudent()))
output2 = rr.Rotate(cf.getStudent())
print("OUTPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n\n {} \n".format(output2))

print ("******************************************************************************")
print ("******************************   PRIVATE PROTECTION   *************************")
print ("******************************************************************************\n")

print("INPUT PRIVATE PROTECTION + HEART TEXT: \n\n {} \n".format(cf.getHeart()))
Zheart, Pheart = pp.PrivateProtection(cf.getHeart())
print("OUTPUT PRIVATE PROTECTION Z + HEART TEXT: \n\n {} \n".format(Zheart))
print("OUTPUT PRIVATE PROTECTION P + HEART TEXT: \n\n {} \n".format(Pheart))


print("INPUT PRIVATE PROTECTION + STUDENT TEXT: \n\n {} \n".format(cf.getStudent()))
Zstudent, Pstudent = pp.PrivateProtection(cf.getStudent())
print("OUTPUT PRIVATE PROTECTION Z + STUDENT TEXT: \n\n {} \n".format(Zstudent))
print("OUTPUT PRIVATE PROTECTION P + STUDENT TEXT: \n\n {} \n".format(Pstudent))



print ("*********************************************************************")
print ("******************************   COMBINED   *************************")
print ("*********************************************************************\n")

Zcombined1, P = pp.PrivateProtection(output1)
Zcombinted2, P = pp.PrivateProtection(output2)

print("OUTPUT RANDOMIZED RESPONSE INTO PRIVATE PROTECTION + OUTPUT1: \n\n {} \n".format(Zcombined1))
print("OUTPUT RANDOMIZED RESPONSE INTO PRIVATE PROTECTION + OUTPUT2: \n\n {} \n".format(Zcombinted2))

