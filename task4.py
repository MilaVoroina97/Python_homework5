# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re
import itertools

first_pol = '5*x^3 + 2*x^2 + 6= 0'
second_pol = '7*x^2+6*x+3 = 0'

def polynomial_parse(polynomial):
    polynomial = polynomial.replace('= 0','')
    polynomial = polynomial.replace('=0','')
    polynomial = re.sub('[*|^| ]',' ',polynomial).split('+')#убираем знаки умножения и т.д. из выражения и разбиваем на отдельные элементы в массиве по знаку плюс
    polynomial = [i.split(' ') for i in polynomial]#делаем список списков, состоящие из отдельных элементов многочлена 
    polynomial = [[j for j in n if j] for n in polynomial]#преобразуем получившийся список списков и убираем лишние элементы, пробелы, которые не относятся к элементам многочлена
    for elem in polynomial:
        if elem[0] == 'x':
            elem.insert(0,1)
        if elem[-1] == 'x':
            elem.append(1)
        if len(elem) == 1:
            elem.append(0)
    polynomial = [tuple(int(char) for char in y if char != 'x') for y in polynomial]
    return polynomial

def polynomial_sum(first,second):
    x = [0] * (max(first[0][1],second[0][1] + 1))
    print(x)
    # for i in first + second:



convert1 = polynomial_parse(first_pol)
convert2 = polynomial_parse(second_pol)
# print(max(convert1[0][1],convert2[0][1]))
#polynomial_sum(convert1,convert2)



