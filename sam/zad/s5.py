list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def convert_to_string(number):
    s = str(number)
    if s.isnumeric() and int(s) == number:
        return s + s[:2]
    return s

def create_set(lst):
    return {convert_to_string(item) for item in lst}

print(create_set(list_1))
print(create_set(list_2))
print(create_set(list_3))