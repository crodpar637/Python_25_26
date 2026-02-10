class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def salario_base(self):
        return self.__salario_base
    @salario_base.setter
    def salario_base(self,nuevo_salario):
        self.__salario_base = nuevo_salario
        
    def calcular_salario(irpf):
        return nuevo_salario - irpf
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Salario Base:{self.calcular_salario}"

class Vendedor(Empleado):
    def __init__(self,nombre,salario_base,ventas_realizadas):
        super().__init__(nombre,salario_base)
        this.ventas_realizadas = list(ventas_realizadas)
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario():
        salario_base + (ventas_realizadas * 0.1)
    def __str__(self):
        return f"Nombre: {self.nombre} - Salario Base: {salario_base} - Ventas: {ventas_realizadas}- Salario Total:{calcular_salario}" 

if __name__ == "__main__":
    empleado = Empleado("Antonio", 3000)
    print(empleado)
    vendedor = Vendedor("Jorge",2000,list(("coche","piso","garaje")))
    print(vendedor)




    

        
        
        

