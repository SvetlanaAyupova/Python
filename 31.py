# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number=int(input('Введите натуральное число: '))
 
factor = []
for i in range(2, int(number**0.5) + 1): # обычно делитель не будет больше корня
    if(number%i==0):
        while (number % i == 0):
            number //= i
            factor.append(i) 
if (number != 1): factor.append(number) 
print(factor)