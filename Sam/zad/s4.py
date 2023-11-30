class CPU:
    def __init__(self, Brand, Models, Cores, Threads):
        self._Brand = Brand
        self.__Models = Models
        self.___Cores = Cores
        self.____Threads = Threads

    def Test_CPU(self):
        print(f"Процессор {self._Brand} {self.__Models} имеет {self.___Cores} ядер и {self.____Threads} потоков")

my_CPU = CPU("Amd", "Ryzen 7", "8", "16")
print(my_CPU._Brand)
my_CPU.Test_CPU()