# Сформировать список из  N членов последовательности
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input('Введите количество членов последовательности: '))

list = [3**i if i % 2 == 0 else -3**i for i in range (N)]
print(list)