class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
            self.__nombre = nombre
    
    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base
    
    
    def calcular_salario(self, irpf):
        parte_irff = self.salario_base * irpf / 100
        return self.salario_base - parte_irff
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Salario base: {self.salario_base}"

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas
    
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario():
        salario_total = salario_base + (ventas_realizadas * 10 / 100)
        return salario_total
        
    def agregar_venta(self, importe):
        print("Agregando venta a la lista")
        ventas_realizadas.append(importe)
        return "Venta agregada correctamente"
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Salario base: {self.salario_base} - Ventas: {self.ventas_realizadas} - Salario total: {self.salario_total}"


def main():
    empleado = Empleado("Jacinto", 1500)
    print(empleado.__str__())
    empleado.nombre = "Pepe"
    print(empleado.calcular_salario(20))
    print(empleado.__str__())    
    
    vendedor = Vendedor("Carlos", 2000, [150,200,80])
    print(vendedor.__str__())
    # vendedor.salario_base = 2300
    # 
    
main()