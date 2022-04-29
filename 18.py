# Реализовать алгоритм перемешивания списка.
import random 
test_list = [1, 2, 3, 4, 5, 6]

print (f'Исходный список: {test_list}')

for i in range(len(test_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    test_list[i], test_list[j] = test_list[j], test_list[i] 

print (f'Перемешанный список: {test_list}')
