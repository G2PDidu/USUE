one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one_max = max(one)
two_max = two.index(max(two))
three_max = three.index(max(three))

one_min = min(one)
two_min = two.index(min(two))
three_min = three.index(min(three))

max_area = (one_max + two_max - three_max) ** 0.5
min_area = (one_min + two_min - three_min) ** 0.5
print(f"Максимальная площадь: {max_area}\nМинимальная площадь: {min_area}")