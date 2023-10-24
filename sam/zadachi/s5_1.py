import math

def s5_1(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
    a = int(input("Введите длину стороны a: "))
    b = int(input("Введите длину стороны b: "))
    c = int(input("Введите длину стороны c: "))

    area = heron_area(a, b, c)

print("Площадь треугольника:", s5_1)