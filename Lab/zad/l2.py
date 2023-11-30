class Car: # Класс для представления автомобиля
    def __init__(self, make, model): # Метод инициализации автомобиля с параметрами: марка и модель
        self.make = make # Свойство класса для хранения марки
        self.model = model # Свойство класса для хранения модели

    def drive(self): # Метод для управления автомобилем
        print(f"Driving the {self.make} {self.model}") # Вывод информации о марке и модели

my_car = Car("Toyota", "Trueno") # Создание экземпляра класса Car с определенными параметрами
my_car.drive() # Управление созданным экземпляром