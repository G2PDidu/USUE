class Car: #Эта строка описывает класс с именем Car. Внутри фигурных скобок содержатся определения методов и переменных, которые принадлежат этому классу.
    def __init__(self, make, model): #Это конструктор класса, который инициализирует его атрибуты. В данном случае он принимает два аргумента: make (марка автомобиля) и model (модель автомобиля).
        self.make = make #Атрибут self.make устанавливается равным аргументу make.
        self.model = model #То же самое происходит с атрибутом model и его аргументом model.

    def drive(self): #Это метод, который “имитирует” вождение автомобиля. Он просто выводит сообщение на экран.
        print(f"Driving the {self.make} {self.model}") #Эта строка выводит на экран информацию о марке и модели автомобиля.

my_car = Car("Toyota", "Trueno") #Здесь создается экземпляр класса Car, который представляет автомобиль марки “Toyota” модели “Trueno”.


print(my_car.make) #Эта строка выводит марку автомобиля, который был создан выше.
my_car.drive() #Вызов метода drive() на Aэкземпляре my_car “имитирует” процесс вождения автомобиля.