'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout
import math
def fun1(matrix):
    maxLen, maxX, maxY=1,0,0
    print(1)
    printMatrix(matrix)
    for idx, val in enumerate(matrix):
        for idy, val2 in enumerate(val):
            if(val2==0):
                print(str(idx)+" "+str(idy))
                printMatrixWithXY(matrix,idx,idy)

def findLongest
 
def printMatrixWithXY(m,idx,idy):
    for a in range(idx,len(m)):
        for b in range(idy,len(m[a])):
            stdout.write(str(m[a][b])+" ")
        stdout.write("\n")
        stdout.flush()

def printMatrix(m):
    printMatrixWithXY(m,0,0)


def getSubMatrix(matrix,x,y):
    newMatrix=[[]]
    for a in range(idx,len(m)):
        for b in range(idy,len(m[a])):
            newMatrix[a-idx,b-idy]=m[a][b]
    return newMatrix
