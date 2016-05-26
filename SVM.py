import random
def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName);
    for line in fr.readlines():
        lineArray = line.strip().split('\t')
        dataMat.append([float(lineArray[0]),float(lineArray[1])])
        labelMat.append(float(lineArray[2]))
    return dataMat, labelMat

def selectJand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j;

def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj

