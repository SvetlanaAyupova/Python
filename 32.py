# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

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
print("Неповторяющийся список: ", list)
