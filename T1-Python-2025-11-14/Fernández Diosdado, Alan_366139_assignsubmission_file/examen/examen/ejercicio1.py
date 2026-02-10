class Empleado():
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, valor):
        self.__salario_base = valor

    def __str__(self):
        return "Nombre "+self.__nombre+" Salario Base: "+str(self.__salario_base)+" euros."

    def calcular_salario(self, irpf):
        salario_nuevo = self.__salario_base - (self.__salario_base * irpf / 100)
        return "Su salario con irpf incluido es de", salario_nuevo, "euros."




class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario(self):
        total_ventas = 0
        for venta in self.__ventas_realizadas:
            total_ventas += venta

        salario_nuevo = self.salario_base + (total_ventas * 10 / 100)
        return salario_nuevo


    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__() + " Ventas:" + str(self.__ventas_realizadas)+" Salario Total: "+  str(self.calcular_salario())

if __name__ == "__main__":
    emp1 = Empleado("Antonio", 100)
    emp2 = Empleado("Fernando", 200)

    ventas_ven1 = [100,150,80]
    ventas_ven2 = [50, 200, 60]
    ven1 = Vendedor("Jose Luis", 100, ventas_ven1)
    ven2 = Vendedor("Angela", 150, ventas_ven2)

    print(emp1)
    print(emp2)
    print(ven1)
    print(ven2)

    ven2.salario_base = 100

    ven2.agregar_venta(75)
    ven2.agregar_venta(15)
    print(ven2)
