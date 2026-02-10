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
        return self.__salario_base * (irpf/100)

    def __str__(self):
        return " - Nombre: " + str(self.__nombre) + " - Salario Base: " + str(self.__salario_base)



class Vendedor(Empleado):

    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        lista_copia = self.__ventas_realizadas.copy()
        return lista_copia

    def calcular_salario(self):
        ventas_totales = sum(self.__ventas_realizadas)
        salario_total = ventas_totales * 0.1 + (super().salario_base) 
        return salario_total
        

    def agregar_ventas(self, importe):
        self.__ventas_realizadas.append(importe)
            
    
    def __str__(self):
        return super().__str__() + "- Ventas: " + str(self.__ventas_realizadas) + " - Salario total: " + str(self.calcular_salario())


def main():
    ventas_realizadas = [100,150,80]
    
    empleado = Empleado("Guillermo", 400.0)
    vendedor = Vendedor("Alan", 500, ventas_realizadas)

    print(empleado.__str__())
    print(vendedor.__str__())

    empleado.nombre = "Manuel"

    vendedor.agregar_ventas(200)
    vendedor.agregar_ventas(50)
    
    print(empleado.__str__())
    print(vendedor.__str__())

main()