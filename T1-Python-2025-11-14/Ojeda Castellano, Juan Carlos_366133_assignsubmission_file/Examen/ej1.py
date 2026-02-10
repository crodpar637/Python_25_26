#a
class Empleado:
    def __init__(self,nombre,salario_base):
        self._nombre=nombre
        self._salario_base=salario_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
        
    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self,salario_base):
        self._salario_base=salario_base

    def calcular_salario(self,irpf):
        return self._salario_base-(self._salario_base*(irpf/100))

    def __str__(self):
        return f"Nombre: {self._nombre} - Salario base: {self._salario_base}"

#b
class Vendedor(Empleado):
    def __init__(self, nombre, salario_base,ventas):
        super().__init__(nombre, salario_base)
        self._ventas=ventas

    @property
    def ventas(self):
        return self._ventas

    def calcular_salario(self):
        return self._salario_base+(self._ventas*0.1)

    def agregar_venta(self,importe):
        self._ventas+=importe
    
    def __str__(self):
        return f"Nombre: {self._nombre} - Salario base: {self._salario_base} - Ventas: {self._ventas} - Salario total: {self.calcular_salario()}"

#c
def main():
    #1
    e=Empleado("Juan",100)
    e2=Empleado("Carlos",120)
    #2
    v=Vendedor("Maria",300,100)
    v2=Vendedor("Angel",200,150)
    #3
    print(e.__str__())
    print(e.__str__())
    print(v.__str__())
    print(v2.__str__())
    #4 (María +150)
    v.agregar_venta(100)
    v.agregar_venta(50)
    #5
    print(e.__str__())
    print(e.__str__())
    print(v.__str__())
    print(v2.__str__())
    

if __name__=="__main__":
    main()