__author__ = 'akashkakumani'
import PrivateProtection as pp
import RandomizedResponse as rr
import ConvertFile as cf

print("INPUT RANDOMIZED RESPONSE + HEART TEXT: \n {} \n".format(cf.getHeart()))
print("OUTPUT RANDOMIZED RESPONSE + HEART TEXT: \n {} \n".format(rr.Rotate(cf.getHeart())))

print("INPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n {} \n".format(cf.getStudent()))
print("OUTPUT RANDOMIZED RESPONSE + STUDENT TEXT: \n {} \n".format(rr.Rotate(cf.getStudent())))


print("INPUT PRIVATE PROTECTION + HEART TEXT: \n {} \n".format(cf.getHeart()))
Z, P = pp.PrivateProtection(cf.getHeart())
print("OUTPUT PRIVATE PROTECTION Z + HEART TEXT: \n {} \n".format(Z))
print("OUTPUT PRIVATE PROTECTION P + HEART TEXT: \n {} \n".format(P))



print("INPUT PRIVATE PROTECTION + STUDENT TEXT: \n {} \n".format(cf.getStudent()))
Z, P = pp.PrivateProtection(cf.getStudent())
print("OUTPUT PRIVATE PROTECTION Z + STUDENT TEXT: \n {} \n".format(Z))
print("OUTPUT PRIVATE PROTECTION P + STUDENT TEXT: \n {} \n".format(P))
