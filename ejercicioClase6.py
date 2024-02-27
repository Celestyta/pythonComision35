from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    @abstractmethod
    def calcular_salario(self):
        pass

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico

    def calcular_salario(self):
        anios_en_empresa = 2024 - self.anio_ingreso
        if anios_en_empresa < 2:
            return self.sueldo_basico
        elif 2 <= anios_en_empresa <= 5:
            return self.sueldo_basico * 0.05
        else:
            return self.sueldo_basico * 0.1

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        if salario < self.salario_minimo:
            return self.salario_minimo
        return salario

# Crear empleados
empleados = [
    EmpleadoFijo(1, "Juan", "Perez", 2019, 1000),
    EmpleadoFijo(2, "Maria", "Lopez", 2017, 1200),
    EmpleadoComision(3, "Pedro", "Gomez", 2020, 800, 10, 50),
    EmpleadoComision(4, "Laura", "Rodriguez", 2018, 900, 8, 60),
    EmpleadoFijo(5, "Luis", "Gonzalez", 2015, 1500),
    EmpleadoComision(6, "Ana", "Martinez", 2019, 1000, 12, 40),
    EmpleadoComision(7, "Carlos", "Sanchez", 2016, 1100, 15, 45),
    EmpleadoFijo(8, "Elena", "Fernandez", 2014, 1800),
    EmpleadoComision(9, "Sofia", "Ramirez", 2021, 700, 6, 55),
    EmpleadoComision(10, "Javier", "Diaz", 2013, 2000, 20, 30)
]

# Mostrar salarios
for empleado in empleados:
    print(f"{empleado.get_nombre_completo()}: {empleado.calcular_salario()}")

# Empleado con más clientes captados
empleado_con_mas_clientes = max([e for e in empleados if isinstance(e, EmpleadoComision)], key=lambda x: x.clientes_captados)
print(f"Empleado con mas clientes captados: {empleado_con_mas_clientes.get_nombre_completo()}")