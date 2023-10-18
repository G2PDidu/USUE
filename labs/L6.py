string = 'Лабораторная работа номер 3'
value = input('Ввведите букву которую хотите найти: ')
for i in string:
    if i == value:
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
    else:
        print(f"Буквы '{value}' нет в указанной строке")