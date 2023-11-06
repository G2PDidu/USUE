def max_element(numbers):
    return max(numbers)

tests = [
    ([2, 3, 4], 4),
    ([5, 6], 6),
    ([7, 8, 9], 9),
]

for numbers, expected_max in tests:
    actual_max = max_element(numbers)
    print(f"Для списка {numbers} максимальный элемент равен {actual_max}, что совпадает с ожидаемым значением {expected_max}")