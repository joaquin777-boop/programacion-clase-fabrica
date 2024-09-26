import datetime

class Empleado:
    def __init__(self, nombre, id_empleado, fecha_contratacion):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.fecha_contratacion = fecha_contratacion

    def calcular_antiguedad(self):
        hoy = datetime.date.today()
        antiguedad = hoy - self.fecha_contratacion
        return antiguedad.days // 365

    def calcular_salario(self):
        pass  # Método abstracto

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id_empleado}")
        print(f"Fecha de contratación: {self.fecha_contratacion}")
        print(f"Antigüedad: {self.calcular_antiguedad()} años")
        print(f"Salario: {self.calcular_salario()}")

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, id_empleado, fecha_contratacion, salario_mensual):
        super().__init__(nombre, id_empleado, fecha_contratacion)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id_empleado, fecha_contratacion, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, id_empleado, fecha_contratacion)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Ejemplo de uso
empleado1 = EmpleadoAsalariado("Juan Pérez", 123, datetime.date(2020, 1, 1), 3000)
empleado2 = EmpleadoPorHoras("María López", 456, datetime.date(2022, 3, 15), 160, 20)

empleado1.mostrar_informacion()
empleado2.mostrar_informacion()
