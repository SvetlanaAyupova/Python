# Задать список из n чисел последовательности (1+1/n)^n
# и вывести на экран их сумму.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension

n = int(input('Введите целое число: '))

list = [round((1+1/x)**x, 2) for x in range(1,n+1)]

print (f'Список: {list}')
print(f'Сумма элементов списка: {sum(list)}')