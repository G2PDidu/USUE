def read_data():
    try:
        with open("transactions.txt", "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "Нет данных для чтения!"

def write_data(data):
    try:
        with open("transactions.txt", "w") as file:
            file.write(data)
    except PermissionError:
        print("Ошибка разрешения! Пожалуйста, повторите попытку позже.")

def main():
    data = read_data()
    transactions = data.split("\n")
    print("Текущие операции: ")
    for transaction in transactions:
        if transaction != "":
            print(transaction)
        else:
            pass

    while True:
        amount = input("Введите сумму транзакции (Enter для выхода): ")
        if amount == "":
            break
        transactions.append(amount)
        write_data("\n".join(transactions))
        print(f"Добавлена транзакция:  {amount}")

if __name__ == "__main__":
    main()