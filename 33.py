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

