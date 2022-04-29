# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

spisok = []
n = int(input('Введите длину списка: '))
for i in range (n):
    spisok.append(random.randint(1,10))
print (f'Cписок:{spisok}')
sum = 0
for i in range (n):
    if i%2>0:
        sum = sum + spisok[i]
print (f'Сумма чисел, стоящих на нечётных позициях = {sum}')
