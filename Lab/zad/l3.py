class Car: #Он определяет основные характеристики автомобиля, такие как марка и модель. Также он имеет метод drive(), который выводит на экран сообщение о том, что автомобиль едет.
    def __init__(self, make, model): #Это конструктор класса. Он инициализирует атрибуты make и model для каждого экземпляра класса.
        self.make = make #Эта строка устанавливает атрибут make для экземпляра класса.
        self.model = model #Эта строка делает то же самое для атрибута model.
    def drive(self): #Данный метод имитирует процесс вождения автомобиля.
        print(f"Driving the {self.make} {self.model}") #Эта строка выводит информацию о марке и модели автомобиля на экран.
my_car = Car("Toyota", "Trueno") #Здесь создается экземпляр класса Car с маркой Toyota и моделью Trueno.
my_car.drive() #Вызов метода drive() для экземпляра my_car имитирует процесс управления автомобилем.
class ElectricCar(Car): #Этот класс наследует все методы и атрибуты от класса Car и добавляет новые.
    def __init__(self, make, model, battery_capacity): #Конструктор этого класса принимает дополнительные параметры: емкость аккумулятора.
        super().__init__(make, model) #Вызывается конструктор родительского класса для инициализации атрибутов make и model.
        self.battery_capacity = battery_capacity #Атрибут battery_capacity присваивается экземпляру класса.
    def charge(self): #имитирует зарядку аккумулятора.
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity}  kWh") #Вывод информации о процессе зарядки на экран.
my_electric_car = ElectricCar("Telsa", "Model S", 75) #Создание экземпляра класса ElectricCar с маркой Telsa, моделью Model S и емкостью аккумулятора 75 kWh.
my_electric_car.drive() #