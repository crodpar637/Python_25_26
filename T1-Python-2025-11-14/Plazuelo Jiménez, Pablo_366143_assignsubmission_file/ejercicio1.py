class Empleado():
    def __init__(self, nombre, salario_base):
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
        salario = self.salario_base - self.salario_base*(irpf/100)
        return salario

    def __str__(self):
        return f"Nombre: {self.nombre} - Salario base: {self.salario_base}"

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas):
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas
        
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas.copy()

    def calcular_salario(self):
        total_ventas = sum(self.ventas_realizadas)
        salario = self.salario_base + (total_ventas*10/100)
        return salario

    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return super().__str__()+f" - Ventas: {self.ventas_realizadas} - Salario total: {self.calcular_salario()}"

#Crea dos objetos de cada clase
empleado = Empleado("Paco", 200)
vendedor = Vendedor("Juan", 230, [50,50])

#Muestra la informacion de cada empleado y vendedor creado
print(empleado)
print(vendedor)

#Modifica algun atributo usando setters
empleado.salario_base = 215
vendedor.salario_base = 250

#Agrega dos ventas a uno de los objetos de la clase Vendedor
vendedor.agregar_venta(20)
vendedor.agregar_venta(40)

#Vuelve a mostrar la informacion actualizada
print(empleado)
print(vendedor)