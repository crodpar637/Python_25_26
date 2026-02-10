
class Empleado:
    def __init__(self,nombre,salario_base):
        self.__nombre=nombre
        self.__salario_base=salario_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def nombre(self,valor):
        self.salario_base=valor

    def calcular_salario(self,irpf):
        return (self.salario_base-irpf)

    
    def __str__(self):
        return f"Nombre: {self.__nombre}- Salario base: {self.__salario_base}"

class Vendedor(Empleado):
    def __init__(self,nombre,salario_base,ventas_realizadas):
        super().__init__(nombre,salario_base)
        self.__ventas_realizadas=[]

    @property
    def ventas_realizadas(self):
        copia=self.__ventas_realizadas
        return copia


    def calcular_salario(self):
        porcentaje_ventas=0
        suma=0
        for a in self.__ventas_realizadas():
            suma+=a
        porcentaje_ventas=suma*(10/100)
        return (self.__salario_base+porcentaje_ventas)

    def agregar_venta(self,importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return f"{super().__str__()}- Ventas: {self.__ventas_realizadas}- Salario total: {self.calcular_salario()}"


def main():

    e1=Empleado("jorge",13.4)
    e2=Empleado("pepe",10.4)

    v1=Vendedor("jorge",13.4,[30.0,999.0,1.0])
    v2=Vendedor("pepe",10.4,[30.0,999.0,1.0])

    print(f"{e1.__str__()}")
    print(f"{e2.__str__()}")

    print(f"{v1.__str__()}")
    print(f"{v2.__str__()}")

    e1.nombre="jon"
    print(f"{e1}")

    print(f"{v1.agregar_venta(1.9)}")
    print(f"{v1.agregar_venta(2.9)}")
    
    print(f"{v1.__str()}")

if __name__=="__main__":
    main()