# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую 
# последовательность. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7] 

#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]
def max_sequence(arr):
    elem = arr[0]
    for i in range(len(arr)):
        if elem in arr:
            elem += 1
        seq = [min(arr),elem - 1]
    return seq

numbers =  [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ]
print(len(numbers))
seq_1 = []
for i in range(len(numbers)):
    if numbers[i] + 1 in numbers:
        if numbers[i] not in seq_1:
            seq_1.append(numbers[i])
            seq_1.append(numbers[i] + 1)
print(seq_1)
seq_2 = (max_sequence(seq_1))
print(f'Максимальная возрастающая последовательность - от {seq_2[0]} до {seq_2[1]}')


