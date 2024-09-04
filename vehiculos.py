# Clase base Vehiculo
class Vehiculo:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.10
            self.precio -= descuento
            print(f"Descuento aplicado. Nuevo precio: {self.precio}")

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)  # Las motos tienen 2 llantas

# Clase Carro que hereda de Vehiculo
class Carro(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)  # Los carros tienen 4 llantas

# Crear objetos de Moto y Carro
moto = Moto(color="Rojo", precio=120000)
carro = Carro(color="Azul", precio=95000)

# Mostrar atributos de la moto
print("Datos de la Moto:")
moto.mostrar_atributos()
moto.aplicar_descuento()  # Aplicar descuento si corresponde
print()  # Línea en blanco para separar salida

# Mostrar atributos del carro
print("Datos del Carro:")
carro.mostrar_atributos()
carro.aplicar_descuento()  # Aplicar descuento si corresponde
