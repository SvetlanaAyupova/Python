n = input('Введите вещественное число: ')
m = n.replace('.', '')
sum = 0
for x in m:
    sum = sum + int (x)
print (sum)
