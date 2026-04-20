
class computer:


    brand = 'Abhay AI'

    def __init__(self, cpu, ram, hdd, vram, gpu):
        print('init method called')
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.vram = vram
        self.gpu = gpu


    def config(self):
        print('config :', self.cpu, self.ram, self.hdd, self.vram, self.gpu)


    @classmethod # class method is used to access class variables and methods without creating an object of the class
    def info(cls):
        return cls.brand


comp1 = computer('i5', '16GB', '512GB', '8GB VRAM', 'NVIDIA GTX 4050')
comp2 = computer('i9', '64GB', '2TB', '32GB VRAM', 'NVIDIA RTX 4090')


comp1.config()
comp2.config()

print(computer.info())


