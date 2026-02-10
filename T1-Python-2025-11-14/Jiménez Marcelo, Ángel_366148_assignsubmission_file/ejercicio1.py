class Empleado:
    
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base
        
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

    def calcular_salario(irpf):
        mult_irpf = irpf / 100
        return self.__salario_base * (1 - mult_irpf)

    def __str__(self):
        return "Nombre: "+self.__nombre+" - Salario base: "+str(self.__salario_base)

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas.copy()
        
    def calcular_salario(self):
        bonificacion = 0
        for venta in self.__ventas_realizadas:
            bonificacion = bonificacion + venta * 0.1
        return (super().salario_base) + (bonificacion)

    def agregar_venta(self, importe):
        return self.__ventas_realizadas.append(importe)

    def __str__(self):
        return "Nombre: " + super().nombre + " - Salario base: " + str(super().salario_base) + " - Ventas: " + str(self.__ventas_realizadas) + "Salario total: " + str(self.calcular_salario())

if __name__ == "__main__":
    j = Empleado("Javi", 1500)
    print(j)
    c = Empleado("Carlos", 2000)
    print(c)
    i = Vendedor("Inma", 1700, [10, 60, 30])
    print(i)
    m = Vendedor("Marta", 1900, [100, 150, 50])
    m.nombre = "Marina"
    print(m)
    i.agregar_venta(100)
    print(i)
    