# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.
n = int(input('Введите целое число: '))
list = []
sum = 0
for x in range(1,n+1):
    y = round((1+1/x)**x, 2)
    sum = sum+y
    number = list.append(y)
print (f'Список: {list}')
print(f'Сумма элементов списка: {sum}')