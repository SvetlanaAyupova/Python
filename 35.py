#35 В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найти его. 

file = open ('numbers.txt', 'w')
file.write ('0 1 2 3 5 6 7 8')

file = open('numbers.txt', 'r')
strnumbers = file.readline()
print(strnumbers)

splitnum = strnumbers.split()

for i in range (0, len(splitnum)):
    if int(splitnum[i]) + 1 != i + 1:
        findnum = i
        break
    
print(findnum)
file.close
