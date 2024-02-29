from enum import Enum

class TipoInstrumento(Enum):
    A = "Percusión"
    B = "Viento"
    C = "Cuerda"

class Instrumento:
    def _init_(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo

class Sucursal:
    def _init_(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def quitarInstrumento(self, instrumento):
        self.instrumentos.remove(instrumento)

class Fabrica:
    def _init_(self):
        self.sucursales = []

    def listarInstrumentos(self):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                print(f"Sucursal: {sucursal.nombre}, ID: {instrumento.id}, Precio: {instrumento.precio}, Tipo: {instrumento.tipo.value}")

    def instrumentosPorTipo(self, tipo):
        instrumentos_filtrados = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipo:
                    instrumentos_filtrados.append(instrumento)
        return instrumentos_filtrados

    def borrarInstrumento(self, id):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.id == id:
                    sucursal.quitarInstrumento(instrumento)
                    return

    def porcInstrumentosPorTipo(self, nombre_sucursal):
        porcentajes = {}
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                total_instrumentos = len(sucursal.instrumentos)
                tipos = {}
                for instrumento in sucursal.instrumentos:
                    tipo = instrumento.tipo
                    if tipo in tipos:
                        tipos[tipo] += 1
                    else:
                        tipos[tipo] = 1
                for tipo, cantidad in tipos.items():
                    porcentaje = (cantidad / total_instrumentos) * 100
                    porcentajes[tipo] = porcentaje
                break
        return porcentajes

# Creé la fábrica de instrumentos
factory = Fabrica()

# Creé tres instrumentos para cada sucursal
instrumento1 = Instrumento("1", 100, TipoInstrumento.A)
instrumento2 = Instrumento("2", 150, TipoInstrumento.B)
instrumento3 = Instrumento("3", 200, TipoInstrumento.C)

# Creé las sucursales y les agregamos los instrumentos
sucursal1 = Sucursal("Sucursal 1")
sucursal1.agregarInstrumento(instrumento1)
sucursal1.agregarInstrumento(instrumento2)
sucursal1.agregarInstrumento(instrumento3)

sucursal2 = Sucursal("Sucursal 2")
sucursal2.agregarInstrumento(Instrumento("4", 120, TipoInstrumento.A))
sucursal2.agregarInstrumento(Instrumento("5", 180, TipoInstrumento.B))
sucursal2.agregarInstrumento(Instrumento("6", 220, TipoInstrumento.C))

sucursal3 = Sucursal("Sucursal 3")
sucursal3.agregarInstrumento(Instrumento("7", 130, TipoInstrumento.A))
sucursal3.agregarInstrumento(Instrumento("8", 160, TipoInstrumento.B))
sucursal3.agregarInstrumento(Instrumento("9", 210, TipoInstrumento.C))

# Agregué las sucursales a la fábrica
factory.sucursales.append(sucursal1)
factory.sucursales.append(sucursal2)
factory.sucursales.append(sucursal3)

# Ejemplo de uso
factory.listarInstrumentos()
print(factory.instrumentosPorTipo(TipoInstrumento.C))
factory.borrarInstrumento("2")
factory.listarInstrumentos()
print(factory.porcInstrumentosPorTipo("Sucursal 1"))