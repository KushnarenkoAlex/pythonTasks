'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout
from matrixUtil import *

def find_longest_line_in_matrix(matrix):
    max_len = 0
    print_matrix(matrix)
    for idx, val in enumerate(matrix):
        for idy, val2 in enumerate(val):
            if(max(max_len,idx+1,idy+1)==max_len):
                return max_len
            if(val2==0):
                tempLen=find_longest_line_in_matrix_from_begin(sub_matrix(matrix,idx,idy))
                max_len=max(max_len,tempLen)
    return max_len

def find_longest_line_in_matrix_from_begin(m):
    hor=count_zero_inline_with_step(m,1,0)
    ver=count_zero_inline_with_step(m,0,1)
    dia=count_zero_inline_with_step(m,1,1)
    return max(hor, ver, dia)

def count_zero_inline_with_step(m,step_horizontal,step_vertical):
    current_x, current_y =0 ,0
    length=1
    while (current_x<len(m)) and (current_y<len(m[0])):
        current_x+=step_horizontal
        current_y+=step_vertical
        if(m[current_x][current_y]==0):
            length+=1
        else:
            break
    return length
