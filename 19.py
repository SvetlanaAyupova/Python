# Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел.
import time

x= time.time()
timespot = str (x)
ran = ''
num = int(input('Введите количество цифр в случайном числе: '))
for i in range (-num, 0):
    ran = ran + timespot[i]
print (ran)
