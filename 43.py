# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

sequence = []
for i in range(10):
    sequence.append(randint(0, 10))
print("Исходный список: ", sequence)

def non_repeated(a):
    d = {}
    non_repeated = []
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for x in d:
        if d[x] == 1:
            non_repeated.append(x)
    return non_repeated

list = non_repeated(sequence)
print("Уникальные элементы: ", list)