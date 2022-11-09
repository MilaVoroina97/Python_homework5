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
    'Тот, кто заберет последнюю конфету - выигрывает и забирает все конфеты оппонента\n')
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
                step = int(input(f'Можно взять кол-во конфет не более {max_number_of_candy} за один раз, у нас осталось всего {all_candies} конфет, введите кол-во конфет еще раз:  '))
            all_candies = all_candies - step
        if all_candies > 0:
            print(f'Еще остались конфеты в количестве {all_candies} конфет')
            counter = 1
        else:
            print('Конфет больше не осталось')

        if counter == 1:
            step = int(input(f'{choice(answers)} {second} = '))
            if step > all_candies or step > max_number_of_candy:
                step = int(input(f'Можно взять кол-во конфет не более {max_number_of_candy} за один раз, у нас осталось всего {all_candies} конфет, введите кол-во конфет еще раз:  '))
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

# two_players()

def bot_and_player():
    all_candies = 2021
    max_number_of_candy = 28
    first_player = input('Введите свое имя: ')
    second_player = 'Bot'
    players = [first_player,second_player]
    print(f'{players[0]} и {players[1]} давайте начинать игру)')
    print('Сначала будет жеребьевка')
    turn = randint(-1,0)
    print(f'Первым ходит игрок {players[turn + 1]}')
    while all_candies > 0:
        turn += 1
        if players[turn % 2] == 'Bot':
            step = all_candies % (max_number_of_candy + 1)
            print(f'Бот забрал {step} конфет из {all_candies}')
        else:
            step = int(input(f'Очередь игрока {players[turn % 2]}, {choice(answers)} : '))
            if step > all_candies or step > max_number_of_candy:
                print(f'Можно взять кол-во конфет не более {max_number_of_candy} за один раз, у нас осталось всего {all_candies} конфет')
                chance = 3
                while chance > 0:
                    if all_candies >= step <= max_number_of_candy:
                        break
                    print(f'Введите кол-во конфет еще раз, у Вас осталось {chance} попыток.')
                    step = int(input())
                    chance -= 1
                else:
                    return print('У Вас больше не осталось попыток, игра окончнена((')
        all_candies -= step
        if all_candies > 0:
            print(f'Осталось еще {all_candies} конфет')
        else:
            print('Конфет больше не осталось')
    print(f'Победил игрок {players[turn %2]} и он забирает все конфеты')


bot_and_player()

    





