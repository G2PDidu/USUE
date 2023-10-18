numbers = [1, 3, 5, 7, 9, 12, 15, 18, 27, 317]
value = int(input('Введите переменную: '))
if value in numbers:
    if value % 2 == 0:
        print('Переменная четная и есть в массиве numbers')
    else:
        print('Переменная нечетная и есть в массиве numbers')
else:
    print(f"Переменной нет в массиве numbers и она равна {value}")