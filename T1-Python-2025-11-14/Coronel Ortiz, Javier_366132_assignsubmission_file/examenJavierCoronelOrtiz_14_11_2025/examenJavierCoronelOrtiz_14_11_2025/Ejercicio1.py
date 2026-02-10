class Empleado:
    
    def __init__(self, nombre, salario_base):
        self.__nombre__ = nombre
        self.__salario_base__ = salario_base
    
    @property
    def nombre(self):
        return self.__nombre__
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre__ = nombre
    
    @property
    def salario_base(self):
        return self.__salario_base__
    
    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base__ = salario_base
    
    def calcular_salario(self, irpf):
        return self.__salario_base__ * (100-irpf)/100
        
    def __str__(self):
        return "Nombre: " + self.__nombre__ + " - Salario base: " + str(self.__salario_base__)

class Vendedor(Empleado):

    def __init__(self, nombre, salario_base, ventas_realizadas):
        Empleado.__init__(self, nombre, salario_base)
        self.__ventas_realizadas__ = ventas_realizadas
        
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas__.copy()
    
    def calcular_salario(self):
        return self.__salario_base__ * (100+10)/100

    def agregar_venta(self, importe):
        self.__ventas_realizadas__.append(importe)

    def __str__(self):
        return Empleado.__str__(self) +  " - Ventas: " + str(self.__ventas_realizadas__) + " - Salario total: " + str(self.calcular_salario())

def main():
    (empleado1, empleado2, vendedor1, vendedor2) = (Empleado("Juan",1000),Empleado("Julia",1250),Vendedor("Juana",1500, [123,321]),Vendedor("Carlos",2000, [456,654]))
    
    print(empleado1)
    print(empleado2)
    print(vendedor1)
    print(vendedor2)
    
    empleado1.salario_base = 1100
    empleado2.nombre = "Julia Rodriguez"
    vendedor1.salario_base = 1200
    vendedor2.nombre = "Carlos Rodriguez"
    
    vendedor1.agregar_venta(100)
    vendedor1.agregar_venta(11)
    
    vendedor2.agregar_venta(200)
    vendedor2.agregar_venta(22)
    
    print(empleado1)
    print(empleado2)
    print(vendedor1)
    print(vendedor2)


if __name__ == "__main__":
    main()

