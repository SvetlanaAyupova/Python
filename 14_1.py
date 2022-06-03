# Подсчитать сумму цифр в вещественном числе.
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension

n = input('Введите вещественное число: ')

sum = sum(map(int, n.replace('.', '')))

print (sum)