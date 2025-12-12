# Superclase
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print("Sonido de animal")


# Subclase Vaca
class Vaca(Animal):
    def sonido(self):
        print(f"{self.nombre}: Muuuu")


# Subclase Lobo
class Lobo(Animal):
    def sonido(self):
        print(f"{self.nombre}: Auuuu")


# Prueba del polimorfismo
a1 = Vaca("Lola")
a2 = Lobo("Colmillo")

a1.sonido()   # Lola: Muuuu
a2.sonido()   # Colmillo: Auuuu
