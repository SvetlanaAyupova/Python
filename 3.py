# Вывести на экран числа от -N до N
a = abs(int (input('Введите число: ')))
for i in range (-a, a+1):
    print (i, end=' ')