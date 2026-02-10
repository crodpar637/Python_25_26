class Empleado:
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

    def calcular_salario(self, irpf):
        return self.salario_base-(irpf/100)*self.salario_base
        
    def __str__(self):
        return f"nombre:{self.__nombre},salario base:{self.__salario_base}"


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, ventas_realizadas=[]):# tuve que inicializarlo aquí para poder usarlo en la funcion y que aceptase que era una lista y así poder insertar despues
        super().__init__(nombre, salario_base)
        self.__ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas.copy() #devolvemos copia 

    def calcular_salario(self, irpf):
        total_ventas = sum(self.__ventas_realizadas)
        salario = self.salario_base+(0.1*total_ventas)
        return salario-(irpf/100)*salario

    def agregar_venta(self, importe):
        self.__ventas_realizadas.append(importe)

    def __str__(self):
        return f"nombre:{self.nombre}, salario base: {self.salario_base}, ventas realizadas: {self.ventas_realizadas}"


# Programa principal
if __name__ == "__main__":
    # Crear objetos
    empleado1 = Empleado("guille", 1000)
    empleado2 = Empleado("fran", 800)

    vendedor1 = Vendedor("alan", 1200)
    vendedor2 = Vendedor("miguel", 900)

    # Agregar ventas
    vendedor1.agregar_venta(100)
    vendedor1.agregar_venta(150)

    # Mostrar información inicial
    print(empleado1)
    print(empleado2)
    print(vendedor1)
    print(vendedor2) #no entiendo porque se me ponen las mismas ventas para todos los vendedores si yo solo se la he agregado al vendedor 1

    # Modificar atributos usando setters
    empleado1.nombre = "guilem"
    vendedor2.salario_base = 950

    # Mostrar información actualizada
    print(empleado1)
    print(vendedor2)
