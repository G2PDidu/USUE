predloj = input("Введите предложение: ")
dlina = len(predloj)
lowwer = predloj.lower()

def main():
    masss = lowwer.count('a') + lowwer.count('e') + lowwer.count('i') + lowwer.count('o') + lowwer.count('u')
    skip = lowwer.replace('ugly', 'beauty')
    TheEnd = (lowwer[0] == 't' and lowwer[-1] == 'e')

print("Результаты")
print("↓↓↓↓↓↓↓↓↓↓")
print(f"Длина предложения:  {dlina}")
print(f"Предложение в нижнем регистре:  {lowwer}")