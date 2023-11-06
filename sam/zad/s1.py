def read_checks(check_list):
    counts = {}
    for check in check_list:
        if counts.get(check) is None:
            counts[check] = 1
    else:
        counts[check] += 1
    return counts


check_list = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998]
counts = read_checks(check_list)
print("Выдано чеков:", len(counts))
print("Разных людей:", len(counts.keys()))
max_count = 0
max_check = None
for check, count in counts.items():
    if count > max_count:
        max_count = count
        max_check = check