#26 Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))
value = []
def fibonacci(n):
    fib = 1
    if n < 0:
        fib = fibonacci(n+2) - fibonacci(n+1)
    elif n == 0:
        fib = 0
    elif n > 2:
        fib = fibonacci(n-1) + fibonacci(n-2)
    return fib
for i in range (-n, n+1):
    value.append(fibonacci(i))
print (value)
