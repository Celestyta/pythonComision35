class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "Estoy comiendo"

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "Estoy corriendo"

class Aguila(Animal):
    def volar(self):
        return "Estoy volando"

# Ejemplo de uso de las clases
animal = Animal(cantidad_patas=4, tipo="vertebrado")
print("Animal:")
print("Cantidad de patas:", animal.cantidad_patas)
print("Tipo:", animal.tipo)
print("Comiendo:", animal.comer())

perro = Perro(cantidad_patas=4, tipo="vertebrado", nombre="Firulais", raza="Labrador")
print("\nPerro:")
print("Cantidad de patas:", perro.cantidad_patas)
print("Tipo:", perro.tipo)
print("Nombre:", perro.nombre)
print("Raza:", perro.raza)
print("Comiendo:", perro.comer())
print("Corriendo:", perro.correr())

aguila = Aguila(cantidad_patas=2, tipo="vertebrado")
print("\nÁguila:")
print("Cantidad de patas:", aguila.cantidad_patas)
print("Tipo:", aguila.tipo)
print("Comiendo:", aguila.comer())
print("Volando:", aguila.volar())