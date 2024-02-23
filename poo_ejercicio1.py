class Bicicleta:
    def __init__(self, marca, color, precio):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La bicicleta acelero a {self.velocidad} km/h.")

    def frenar(self, decremento):
        if self.velocidad >= decremento:
            self.velocidad -= decremento
            print(f"La bicicleta freno a {self.velocidad} km/h.")
        else:
            print("La bicicleta ya esta detenida.")

    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f"La bicicleta ahora es de color {self.color}.")

# Ejemplo de uso de la clase Bicicleta
mi_bicicleta = Bicicleta(marca="Trek", color="azul", precio=300)
print(f"Marca: {mi_bicicleta.marca}, Color: {mi_bicicleta.color}, Precio: ${mi_bicicleta.precio}")

mi_bicicleta.acelerar(10)
mi_bicicleta.frenar(5)

mi_bicicleta.pintar("rojo")
print(f"Nuevo color: {mi_bicicleta.color}")