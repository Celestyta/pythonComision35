class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años y es de profesión {self.profesion}."

    def caminar(self):
        return f"{self.nombre} sale a caminar."

class Bicicleta:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def __str__(self):
        return f"una bicicleta {self.color} marca {self.marca}."


# Crear instancia de Persona
juan_lopez = Persona(nombre="Juan Lopez", edad=25, profesion="Abogado")

# Crear instancia de Bicicleta
bicicleta_juan = Bicicleta(color="amarilla", marca="Massino")

# Simular acciones
print(juan_lopez)
print(juan_lopez.caminar())
print(f"También tiene {bicicleta_juan} Y a veces sale a dar vueltas en ella.")