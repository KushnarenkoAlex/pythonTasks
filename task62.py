'''Дана строка, представляющая из себя арифметическое выражение,
состоящее из чисел, скобок и арифметических операций.
Проверьте данное выражение на правильность расстановки скобок.'''

from matrixUtil import *

def check_brackets(string):
    check=0
    for c in string:
        if(c=="("):
            check+=1
        elif (c==")"):
            check-=1
    return check==0
