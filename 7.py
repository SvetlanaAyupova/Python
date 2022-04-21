# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = [True, False]
y = [True, False]
z = [True, False]
check = 1

for i in range (0, 2):
    for j in range (0, 2):
        for k in range (0, 2):
            if (not (x[i] or y[j] or z[k]) == (not x[i] and not y[j] and not z[k])):
                print(f'Выражение из условия - True')
            else:
                print(f'Выражение из условия - False')
                check = 0

if (check == 1):
    print('Выражение ИСТИННО!')
else:
    print('Выражение ЛОЖНО!')