def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

# Пример использования
for number in fib(200):
    print(number)