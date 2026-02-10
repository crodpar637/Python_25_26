class Empleado:
    
    def __init__(self,nombre, salario_base):
        self.__nombre=nombre
        self.__salario_base=salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self,valor):
        self.__salario_base = valor

    def calcular_salario(self,irpf):
        desgrabado = self.__salario_base * irpf / 100
        return self.__salario_base - desgrabado

    def __str__(self):
        return "Nombre: " + self.__nombre + " - Salario base: " + self.__salario_base


class Vendedor(Empleado):

    def __init__(self,nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario(self):
        total10ventas = 0
        for i in self.__ventas_realizadas:
            total10ventas += i

        total10ventas = total10ventas*0.1
        return self.__salario_base + total10ventas

    def agregar_venta(self,importe):

        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__() + " - Ventas: " + self.__ventas_realizadas + " - Salario total: " + self.calcular_salario


if __name__ == "__main__":

    e1 = Empleado('Manuel',1200)
    e2 = Empleado('Sofía',1400)
    v1 = Vendedor('José',1000,[150,300,220])
    v2 = Vendedor('Pepa',1000,[175, 240, 190])

    print(e1)
    print(e2)
    print(v1)
    print(v2)

    e2.salario_base(1500)
    v1.salario_base(1100)

    v2.agregar_venta(230)
    v2.agregar_venta(500)

    print(e1)
    print(e2)
    print(v1)
    print(v2)
        