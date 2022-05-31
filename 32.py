# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

lst = []
for i in range(10):
    lst.append(randint(0, 10))
print("Исходный список: ", lst)

lst1 = []
count = 0
for i in lst:
  if i not in lst1:
    lst1.append(i)
print(f'Неповторяющиеся элементы: {lst1}')