'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout
from matrixUtil import *

def findLongestLineInMatrix(matrix):
    maxLen, maxX, maxY=0,0,0
    printMatrix(matrix)
    for idx, val in enumerate(matrix):
        for idy, val2 in enumerate(val):
            if(max(maxLen,idx+1,idy+1)==maxLen):
                return maxLen
            if(val2==0):
                tempLen=findLongestLineInMatrixFromBegin(getSubMatrix(matrix,idx,idy))
                maxLen=max(maxLen,tempLen)
    return maxLen

def findLongestLineInMatrixFromBegin(m):
    hor=countZeroInlineWithStep(m,1,0)
    ver=countZeroInlineWithStep(m,0,1)
    dia=countZeroInlineWithStep(m,1,1)
    return max(hor, ver, dia)

def countZeroInlineWithStep(m,stepHorizontal,stepVertical):
    currentX, currentY=0, 0
    length=1
    while (currentX<len(m)) and (currentY<len(m[0])):
        currentX+=stepHorizontal
        currentY+=stepVertical
        if(m[currentX][currentY]==0):
            length+=1
        else:
            break
    return length
