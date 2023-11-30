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


class Intel_CPU(CPU):
    def __init__(self, Brand, Models, Cores, Threads, TurboBoost):
        super().__init__(Brand, Models, Cores, Threads)
        self.TurboBoost = TurboBoost

    def boost(self):
        print(f"Процессор {self.Brand} {self.Models} имеет {self.TurboBoost} версии")

al_CPU = Intel_CPU("Intel", "i7-8700", "6", "8", "2.0")
al_CPU.Test_CPU()
al_CPU.boost()