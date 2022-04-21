# Показать первую цифру дробной части числа
#number = float(input('Введите число: '))
#number1=str(float(number))
#number2 = number1.split('.')
#number3 = number2[1]
#number_fin =number3[0]
#print(number_fin)

n = float(input('Введите дробное число: '))
d = int((n*10)%10)
print('Первая цифра дробной части числа: ',d,'\n')