__author__ = 'akashkakumani'
import numpy as np

def getHeart():
    with open('heart.txt') as f:
        lines = f.readlines()
        list = []
        for l in lines:
            tmp = l.split(',')
            tmp[22] = tmp[22].strip('\n')
            for index,n in enumerate(tmp):
                tmp[index] = int(tmp[index])
            list += [tmp]
        f.close()
        return np.asarray(list)


def getStudent():
    with open("student-mat.csv") as csv_file:
        lines = csv_file.readlines()
        list = []
        for l in lines:
            tmp = l.split(';')
            tmp2 = []
            if tmp[1] == '"F"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[5] == '"A"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[14] == 0:
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[15] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[16] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[18] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[19] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[20] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[21] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            if tmp[22] == '"no"':
                tmp2 += [0]
            else:
                tmp2 += [1]
            list += [tmp2]
        return np.asarray(list)


