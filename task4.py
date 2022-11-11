# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re
from itertools import *
import itertools

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
    elem = [0] * (max(first[0][1],second[0][1] + 1))#на основе количества максимальной степени в одном из многочленов, определяем кол-во коэффициентов в сумме двух многочленов
    # print(elem)
    for i in first + second:
        # print(f'0: {i}  {elem[i[1]]}  {i[0]}  ',end ='')
        elem[i[1]] += i[0]#elem[i[1]] - определяет место коэффициента в массиве коэффициентов, если встречаются коэффциенты с одной и той же степенью они складываются
        # print(f'1: {elem[i[1]]} , {i}, {elem}')
    sum = [(elem[i],i) for i in range(len(elem)) if elem[i] != 0]
    sum.reverse()
    return sum

def create_new_pol(res):
    count = ['*x^'] * len(res)
    coeff = [i[0] for i in res]
    stepen = [i[1] for i in res]
    new_pol = [[str(x),str(y),str(z)] for x, y, z in (zip(coeff,count,stepen))]
    # print(new_pol)

    for j in new_pol:
        if j[0] == '0':
            del(j[0])
        if j[-1] == '0':
            del(j[-1])
            del(j[-1])
        if len(j) > 1 and j[0] == '1' and j[1] == '*x^':
            del(j[0])
            j[0] = 'x^'
        if len(j) > 1 and j[-1] == '1':
            del(j[-1])
            j[-1] = '*x'
        j.append(' + ')

    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return ''.join(map(str,new_pol))

first = '7*x^2+6*x+3 = 0'
second = '5*x^3 + 2*x^2+6 = 0'
print('Первоначальный вид многочленов: ')
print(first)
print(second)
convert1 = polynomial_parse(first)
convert2 = polynomial_parse(second)
sum_result  = polynomial_sum(convert1,convert2)
print('Сумма многочленов: ')
print(create_new_pol(sum_result))






