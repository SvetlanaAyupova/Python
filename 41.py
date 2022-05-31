# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные: 12W1B12W3B24W1B14W

with open('Input41.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('Input41.txt', 'r') as data:
    string = data.readline()

# Сжатие данных
count = 1
s = ""
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            s+= str(count) + string[i]
            count = 1
s+= str(count) + string[i]
print(s)

with open('Encode41.txt', 'w') as data:
    data.write(s)

# Восстановление данных

decoded_string = ''
char_amount = ''
for i in range(len(s)):
    if s[i].isdigit():
        char_amount += s[i]
    else:
        decoded_string += s[i] * int(char_amount)
        char_amount = ''
print(decoded_string)


with open('Decode41.txt', 'w') as data:
    data.write(decoded_string)