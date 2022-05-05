# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень: '))
coefficient = []
for i in range(k+1):
    coefficient.append(randint(0, 100))
print("Список коэффициентов: ", coefficient)

file = open ( "polynom.txt", "w+" )
while k >= 0:
    for i in range(len(coefficient)):
        if k > 1 and coefficient[i] != 0:
            file.write(str(coefficient[i]) + '*x^'+ str(k) + '+')
        elif k == 1 and coefficient[i] != 0:
            file.write(str(coefficient[i]) + '*x' + '+')
        elif k == 0 and coefficient[i] != 0:
            file.write(str(coefficient[i]) + ' = 0')
        k=k-1
file.close()

# Второй многочлен для задачи 34

d = int(input('Введите натуральную степень: '))
coefficient1 = []
for i in range(d+1):
    coefficient1.append(randint(0, 100))
print("Список коэффициентов: ", coefficient1)

file = open ( "polynom1.txt", "w+" )
while d >= 0:
    for i in range(len(coefficient1)):
        if d > 1 and coefficient1[i] != 0:
            file.write(str(coefficient1[i]) + '*x^'+ str(d) + '+')
        elif d == 1 and coefficient1[i] != 0:
            file.write(str(coefficient1[i]) + '*x' + '+')
        elif d == 0 and coefficient1[i] != 0:
            file.write(str(coefficient1[i]) + ' = 0')
        d=d-1
file.close()