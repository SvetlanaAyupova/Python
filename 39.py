#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте, как наделить бота "интеллектом"


# 2 игрока

# from random import randint

# candies = int(input('Сколько конфет: '))
# take = int(input("Максимальное количество конфет можно взять: "))

# # сколько нужно взять конфет для победы:
# def take_to_have_for_first(candies, take):
#     take_candies = candies % (take + 1)
#     if take_candies == 0:
#         take_candies = take
#     return(f'чтобы выиграть необходимо взять {take_candies} конфет')

# first_move = randint(1,2) # определяем, кто ходит первым кто вторым
# print(f"Первым ходит игрок {first_move}")
# second_move = 3 - first_move
# print(f'Второй ходит игрок {second_move}')

# count = 0
# while candies > 0:
#     count += 1
#     print(take_to_have_for_first(candies, take))
#     player1 = int(input("Ход первого игрока. Возьмите конфеты: "))
#     candies = candies - player1
#     print(f'осталось конфет: {candies}')
#     if candies > 0:
#         print(take_to_have_for_first(candies, take))
#         player2 = int(input("Ход второго игрока. Возьмите конфеты: "))
#         candies = candies - player2
#         print(f'осталось конфет: {candies}')

# if candies == 0:
#     print('Игра окончена')
# if take % 2 != 0:
#     print(f'Победил игрок {first_move}')
# else:
#     print(f'Победил игрок {second_move}')



# а) Игра против бота (или бота с "интелектом")

from random import *

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!"\n'
            'Основные правила игры: \n'
            'Нам будет дано некоторое количество конфет,\n'
            'за один ход мы можем взять не более определённого количества, \n'
            'о котором мы с вами договоримся. \n'
            'Итак, начнём!\n')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def candy(n):  # выбираем окончание для слова конфеты
    if n == 1 or (n % 10 == 1 and n > 20):
        return 'а'
    elif 1 < n < 5 or 1 < n % 10 < 5:
        return 'ы'
    else:
        return ''


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут? ')
    player2 = 'Бот'
    print(f'Очень приятно, меня зовут {player2}\n')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать? '))
    m = int(input('Сколько максимально будем брать конфет за один ход? '))

    first = input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу')
    if first != '1':
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):

    count = rules[2]  # кто ходит первым

    while rules[0] > 0:
        max = rules[1]
        if max > rules[0]:  # максимальное взятие не должно превышать остаток
            max = rules[0]
        if not count % 2:   # если ход бота
            # а) Бот без "интеллекта"
            # move = randint(1, max)
            # print(f'Я забираю {move} ')

            # б) Бот с "интеллектом"
            move = rules[0] % (rules[1] + 1)
            if move == 0:
                move = rules[1]
            print(f'Я забираю {move} конфет {candy(move)}')
        else:
            # просим человека взять конфеты
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{candy(rules[1])}, у нас всего {rules[0]} конфет{candy(rules[0])}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] -= move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{candy(rules[0])}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)
print (rules)

winer = play_game(rules, players, messages)
print(f'Поздравляю! В этот раз победил(а) {winer}! Ему(Ей) достаются все конфеты!\n')