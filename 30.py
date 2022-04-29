# Вычислить число c заданной точностью d.
# при d = 0.001,π = 3.141    10^(-1) ≤ d ≤ 10^(-10)

from math import pi

d =  input("Введите точность в формате десятичной дроби (в промежутке от 10^(-1) до 10^(-10)): \n")

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

s = get_count(d)
print(f'При d = {d}, π = {round(pi, s)}')