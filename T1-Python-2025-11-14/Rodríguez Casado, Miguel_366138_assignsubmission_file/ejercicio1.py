class Empleado:
    def __init__(self,nombre,salario_base):
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

    def calcular_salario(self,irpf):
        restar = irpf * self.__salario_base / 100
        salario = self.__salario_base - restar
        return salario

    def __str__(self):
        return "Nombre: "+self.__nombre+" - Salario base: "+ str(self.__salario_base)

class Vendedor(Empleado):
    def __init__(self,nombre,salario_base,ventas_realizadas):
        super().__init__(nombre,salario_base)
        self.__ventas_realizadas = ventas_realizadas

    def ventas_realizadas(self):
        copia = self.__ventas_realizadas[:]
        return copia

    def calcular_salario(self,irpf):
        salario = super().calcular_salario(irpf)
        suma = 0
        for i in self.__ventas_realizadas:
            suma += i
        total = 10*suma/100
        salarioT = float(salario + total)
        return salarioT
        
    def agregar_venta(self,importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__()
        #"- Salario Total:" + str(self.calcular_salario())
    

def main():
    empleado = Empleado("Miguel", 100.0)
    print(empleado.__str__())

    vendedor = Vendedor("Sergio", 1000.0, [100,150,80])
    print(vendedor.__str__())

    empleado.nombre = "Carlos"
    
    vendedor.agregar_venta(2.0)
    vendedor.agregar_venta(28.0)

    print(vendedor.__str__())

main()