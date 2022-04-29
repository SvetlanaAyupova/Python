# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#max = 0
#min = 1
#list_of_numbers = [1.1, 1.2, 3.1, 5, 10.01]
#print(f'На входе имеем список чисел:\n{list_of_numbers}')
#for element in list_of_numbers:
#    swap = str(float(element)).split('.')
#    if int(swap[1]):
#        fraction = int(swap[1])/(10**len(swap[1]))
#    if fraction < min:
#        min = fraction
#    if fraction > max:
#        max = fraction
#print(f'Максимальное значение дробной части: {max},\nминимальное значение дробной части: {min}\nразница между максимальной и минимальной частями равна: {max-min}')

list = [1.1, 1.2, 3.1, 5, 10.01] 
print(list, '\n')
list1 = []

for i in range(len(list)):
    if list[i] - round(list[i]) == 0:
        continue
    else:
        list1.append(round(list[i] - round(list[i]), 3))

print(list1)
print('Максимальное число: ', max(list1))
print('Минимальное число: ', min(list1))
print('Разница: ', max(list1) - min(list1))