# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
n = int(input('Введите целое число: '))
list = []
mult = 1
for x in range(1, n+1):
    mult = mult*x
    number = list.append(mult)
print (list)

