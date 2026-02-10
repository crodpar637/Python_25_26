from functools import reduce
class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter#poner el nombre de la propiedad, en los setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def salario_base(self):
        return self.__salario_base
    @salario_base.setter
    def salario_base(self,salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self,irpf):
        return (self.__salario_base - irpf)
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Salario base: {self.__salario_base}"

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario(self):
        sum=0
        #for i in self.__ventas_realizadas:
            #sum +=i

        sum1 = reduce(lambda item1, item2: item1 + item2, self.__ventas_realizadas)
        fin = (sum/10)
        return (self.__salario_base + fin)

    def agregar_venta(self,importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__()+" - Ventas:" +str(self.__ventas_realizadas)


def main():
    l1=[150,28,327]
    l2=[600,75,490]
    
    e1 = Empleado("Adrian", 1000)
    e2 = Empleado("Ruben", 100)
    v1= Vendedor("Pablo", 150, l1)
    v2= Vendedor("Payan", 400, l2)
    print(f"{e1}\n{e2}\n{v1}\n{v2}\n")
    print(e1)
    print(e2)
    print(v1)
    print(v2)
    print("="*80)

    e1.nombre="Diego"#antes era Adrian
    v2.salario_base=600#antes era 400
    
    v1.agregar_venta(4000)
    v1.agregar_venta(687)
    print(f"{e1}\n{e2}\n{v1}\n{v2}\n")

main()