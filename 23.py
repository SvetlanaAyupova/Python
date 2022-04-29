# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
#         [2, 3, 5, 6] => [12, 15]

import random

spisok = []
n = int(input('Введите длину списка: '))
for i in range(n):
    spisok.append(random.randint(1, 10))
print(f'Cписок: {spisok}')

massiv = []

for i in range((len(spisok)+1) //2):
    massiv.append(spisok[i]*spisok[-1-i])
print(massiv)
