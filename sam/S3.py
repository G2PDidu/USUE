def check_range(number):
    if number >= 0 and number <= 3:
        return "Число принадлежит диапазону 0–3"
    elif number > 3 and number <= 6:
        return "Число принадлежит диапазону 4–6"
    else:
        return "Число принадлежит диапазону 7–10"
number = int(input('Введите число: '))
print(check_range(number))