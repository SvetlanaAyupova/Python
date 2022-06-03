# Написать программу получающую набор произведений чисел от 1 до N.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
import math

n = int(input('Введите целое число: '))

numbers = list(map(lambda i: math.factorial (i), range (1, n+1)))
print (numbers)