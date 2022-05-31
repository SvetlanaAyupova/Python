#37 Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих условию предыдущей задачи.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7] 

#from random import *

nums = [1, 5, 2, 3, 4, 6, 1, 7]
#nums = [randint(1,9) for i in range(21)]
#print('Задан список: ', nums)

def get_create (nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups

print('Последовательность: ', get_create (nums))

largest = 0
index = 0

for i in range(len(nums)):
    if len(get_create (nums[i:])) > largest:
        largest = len(get_create (nums[i:]))
        index = i
        
print('Итого, создан список: ', nums[index:])
print('Итого, последовательность: ', get_create (nums[index:]))
