results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

bestThree = sorted(results)[-3:]
worstThree = sorted(results, reverse=True)[-3:]

results10AndAbove = [x for x in results if x >= 10]

print("Три лучшие результаты:", bestThree)
print("Три худшие результаты:", worstThree)
print("Все результаты от 10:", results10AndAbove)