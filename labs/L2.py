ft = int(input('Введите переменую: '))
if ft < 0:
    print('Переменная меньше 0')
elif 0 < ft < 10:
    print('Переменная больше 0 и меньше 10')
else:
    print('Переменная больше 10')