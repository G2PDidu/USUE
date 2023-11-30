class CPU:
    def __init__(self, Brand, Models, Cores, Threads):
        self.Brand = Brand
        self.Models = Models
        self.Cores = Cores
        self.Threads = Threads

    def Test_CPU(self):
        print(f"Процессор {self.Brand} {self.Models} имеет {self.Cores} ядер и {self.Threads} потоков")

my_CPU = CPU("Amd", "Ryzen 7", "8", "16")
my_CPU.Test_CPU()