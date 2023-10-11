class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_info(self):
        print(f"La salud de {self.nombre} es {self.salud} y su felicidad es de {self.felicidad}")
    def alimentar(self, salud, felicidad):
        self.salud += 10
        self.felicidad += 10

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def agregar_león(self, name, edad):
        self.animals.append( León(name,edad,0,0) )
    def agregar_tigre(self, name, edad):
        self.animals.append( Tigre(name,edad,0,0) )
    def imprimir_toda_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.mostrar_info()
    def alimentar_a_todos(self):
        for animal in self.animals:
            animal.alimentar(0, 0)
    
class León(Animal):
    def __init__(self, nombre, edad, salud, felicidad):
        super().__init__(nombre, edad)
        self.salud = 150
        self.felicidad = 50
    def alimentar(self, salud, felicidad):
        self.salud += 30
        self.felicidad += 20

class Tigre(Animal):
    def __init__(self, nombre, edad, salud, felicidad):
        super().__init__(nombre, edad)
        self.salud = 100
        self.felicidad = 85
    def alimentar(self,salud,felicidad):
        super().alimentar(salud, felicidad)

zoo1 = Zoo("El zoo de John")
zoo1.agregar_león("Nala", 14)
zoo1.agregar_león("Simba", 5)
zoo1.agregar_tigre("Rajah", 8)
zoo1.agregar_tigre("Shere Khan", 2)
zoo1.alimentar_a_todos()
zoo1.imprimir_toda_info()