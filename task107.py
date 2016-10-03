'''Некоторые числа можно получить так: взять единицу, а затем
либо умножать результат на 3, либо прибавлять к результату 5.
Например, число 24 получается как (((1*3)+5)*3). Написать функцию, которая
для данного числа создает строку с таким выражением.
'''

def create_expression(number,div,plus):
    result=""
    count=0
    while number!=1 or number<=0:
        var=""
        if number % div == 0:
            number=number/div
            var="*"+str(div)
        else:
            number=number-plus
            var="+"+str(plus)
        count+=1
        result=var+")"+result
    res=''.join(['(' for s in range(count)])
    return res+"1"+result
