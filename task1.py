# задача 1. Создайте программу для игры с конфетами человек против человека.

import random
from random import choice,randint

game_rules = ('"Играем вдвоем с конфетками"\n'
    'В игре могут быть двое участников\n'
    'Первый ход игрока определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры: \n'
    'У нас есть 2021 конфета\n'
    'За один ход можно забрать не более 28 конфет\n'
    'Тот, кто заберет последнюю конфету - проигрывает\n')
print(game_rules)

answers = ['Ваша очередь', 'Теперь Вы можете ходить','Ваш ход',"Теперь Вы можете взять конфету"]

def introduce_players():
    first_player = input('Введите имя первого игрока: ')
    second_player = input('Введите имя второго игрока: ')
    names = []
    names.append(first_player)
    names.append(second_player)
    print(f'Приятно познакомиться {first_player} и { second_player}, давайте начинать игру')
    return names

def two_players():
    all_candies = 2021
    max_number_of_candy = 28
    counter = 0
    players = introduce_players()
    print('Сейчас будет жеребьевка')
    turn = randint(1,2)
    if turn == 1:
        first = players[0]
        second = players[1]
    else:
        first = players[1]
        second = players[0]
    print(f'Первым ходит игрок - {first}')
    while all_candies > 0:
        if counter == 0:
            step = int(input(f'{choice(answers)} {first} = '))
            if step > all_candies or step > max_number_of_candy:
                step = int(input(f'Можно взять кол-во конфет не более {max_number_of_candy} и у нас всего только {all_candies} конфет,поэтому можно взять не более этого числа, введите кол-во конфет еще раз:  '))
            all_candies = all_candies - step
        if all_candies > 0:
            print(f'Еще остались конфеты в количестве {all_candies} конфет')
            counter = 1
        else:
            print('Конфет больше не осталось')

        if counter == 1:
            step = int(input(f'{choice(answers)} {second} = '))
            if step > all_candies or step > max_number_of_candy:
                step = int(input(f'Можно взять кол-во конфет не более {max_number_of_candy} и у нас всего только {all_candies} конфет,поэтому можно взять не более этого числа, введите кол-во конфет еще раз:  '))
            all_candies = all_candies - step
        if all_candies > 0:
            print(f'Еще остались конфеты в количестве {all_candies} конфет')
            counter = 0
        else:
            print('Конфет больше не осталось')
    if counter == 1:
        print(f'Игрок {second} выиграл')
    if counter == 0:
        print(f'Игрок {first} выиграл')





