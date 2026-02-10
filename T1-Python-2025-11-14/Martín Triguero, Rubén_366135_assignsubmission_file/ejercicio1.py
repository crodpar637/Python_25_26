class Empleado:
    def __init__(self, nombre, salario_base ):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self,salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self, irpf):
        return self.__salario_base - (self.__salario_base * irpf / 100)

    def __str__(self):
        return "Nombre: "+ self.__nombre +" - Salario base: "+ str(self.__salario_base)


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas ):
        Empleado.__init__(self, nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas[:]

    @ventas_realizadas.setter
    def ventas_realizadas(self,ventas_realizadas):
        self.__ventas_realizadas = ventas_realizadas

    def calcular_salario(self):
        total_ventas = 0.0
        for venta in self.__ventas_realizadas:
            total_ventas += venta
        return self.salario_base + (total_ventas * 10 / 100)

    def __str__(self):
        return "Nombre: "+ self.nombre +" - Salario base: "+ str(self.salario_base) + " - Ventas: "+ str(self.__ventas_realizadas) + "- Salario total: "+ str(self.calcular_salario())

    def agregar_venta(self,importe):
        self.__ventas_realizadas.append(importe)


#Ejecución del programa principal
if __name__ == "__main__":
    empleado1 = Empleado("Ruben", 1700.0)
    print("Empleado 1: " + str(empleado1))
    
    empleado2 = Empleado("Adrian", 2500.0)
    print("Empleado 2: " + str(empleado2))
    empleado1.salario_base = 1500.0
    print("Empleado 1 con el salario base cambiado: " + str(empleado1))

    print("Salario calculado de empleado1: "+ str(empleado1.calcular_salario(15)))
    print("Salario calculado de empleado2: "+ str(empleado2.calcular_salario(15)))

    ventas_realizadas_diego = [100.0,150.0,80.0]
    ventas_realizadas_jose = [400.0,170.0,90.0]

    vendedor1 = Vendedor("Diego", 1700.0, ventas_realizadas_diego)
    print("Vendedor 1: " + str(vendedor1))
    
    vendedor2 = Vendedor("Jose Manuel", 2500.0, ventas_realizadas_jose)
    print("Vendedor 2: " + str(vendedor2))
    
    vendedor2.nombre = "Juanito"
    print("Vendedor 2 con nombre cambiado: " + str(vendedor2))

    vendedor1.agregar_venta(90.50)
    vendedor1.agregar_venta(130.95)

    vendedor2.agregar_venta(120.87)
    vendedor2.agregar_venta(130.60)

    print("Vendedor 1 con nuevas ventas: " + str(vendedor1))
    print("Vendedor 2 con nuevas ventas: " + str(vendedor2))


    

    