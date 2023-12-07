def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

# Пример использования
for number in fib(200):
    print(number)

def write_fibs_to_file(n):
    file = open("fib.txt", "w")
    a, b = 0, 1
    for _ in range(n):
        file.write(str(a) + "\n")
        a, b = b, a + b
    file.close()


#Пример использования
write_fibs_to_file(200)