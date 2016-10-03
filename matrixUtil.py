'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout

def print_matrix(m):
    for a in range(len(m)):
        for b in range(len(m[a])):
            stdout.write(str(m[a][b])+" ")
        stdout.write("\n")
        stdout.flush()

def sub_matrix_from_point_to_end(m,x,y):
    return sub_matrix(m,x,y,len(m),len(m[0]))

def sub_matrix(m,x1,y1,x2,y2):
    new_matrix=[]
    for a in range(x2-x1):
        temp=[]
        for b in range(y2-y1):
            temp.append(m[a+x1][b+y1])
        new_matrix.append(temp)
    return new_matrix
