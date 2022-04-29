# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
n = int(input('Введите целое число: '))
pos = input (f'Введите через запятую позиции элементов не более n*2: ').split(',')
with open ('file.txt', 'w') as file:
    for i in pos:
        file.write (f'{i}\n')
spisok = []
for i in range (-n,n+1):
    spisok.append (i)
print (spisok)

mult = 1
with open ('file.txt', 'r') as file:
    for y in file:
        mult = mult*spisok[int(y.strip())]
print (f'Произведение элементов с введенными позициями равно: {mult}')