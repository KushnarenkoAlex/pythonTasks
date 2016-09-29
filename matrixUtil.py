'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout

def printMatrix(m):
    for a in range(len(m)):
        for b in range(len(m[a])):
            stdout.write(str(m[a][b])+" ")
        stdout.write("\n")
        stdout.flush()

def getSubMatrix(m,x,y):
    newMatrix=[]
    for a in range(len(m)-x):
        temp=[]
        for b in range(len(m[a])-y):
            temp.append(m[a+x][b+y])
        newMatrix.append(temp)
    return newMatrix
