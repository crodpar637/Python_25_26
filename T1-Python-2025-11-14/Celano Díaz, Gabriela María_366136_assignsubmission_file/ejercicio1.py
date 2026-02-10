class Empleado:
    #constructor
    def __init__(self,nombre,salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base
    
    #getters y setters
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def salario_base(self):
        return self.__salario
    @salario_base.setter
    def salario_base(self,salario_base):
        self.__salario_base = salario_base

    def calcular_salario(self,irpf):
        salario_irpf = self.__salario_base -(self.__salario_base*irpf/100)
        print(str(salario_irpf))
        return salario_irpf

    def __str__(self):
        return f"Nombre: {self.__nombre} -Salario Base: {self.__salario_base}"
        

class Vendedor(Empleado):
    #constructor
    def __init__(self, nombre,salario_base,ventas_realizadas):
        super().__init__(nombre,salario_base)
        self.__ventas_realizadas = ventas_realizadas
    
    #getter
    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas
    
    #una propiedad de solo lectura NO SETTER devuelve la copia de la lista.???   
    #@ventas_realizadas.setter
    def ventas_realizadas(self,ventas_realizadas):
       copia_lista = self.__ventas_realizadas
       return copia_lista
        
    #sobreescribe el metodo calcular /ventas es una lista de float.
    def calcular_salario(self):
        # sumar las ventas   #for recorro la lista 
        total_ventas = 0
        for x in ventas_realizadas:
            total_ventas += x
        
        salario_total = self.__salario_base + (total_ventas *0.10)
        return salario_total

    #string
    def __str__(self):                      
        return super().__str__() + f" Ventas: {total_ventas} - Salario total: {salario_total}"

if __name__ == "__main__":

    empleado = Empleado("Jose", "10000")

    ventas_vendedor = [100.0,200.0,300.0,500.0]
    vendedor = Vendedor("David",1000,ventas_vendedor)
    print(empleado)
    print(vendedor)
    #modificar un atributo utilizando setters:
    empleado.nombre = "Ana"
    #agrega dos ventas a uno de los objetos de la clase vendedor
    ventas_realizadas().append(600)
    ventas_realizadas().append(700)
    # info actualizada
    print(empleado)
    print(vendedor)
   
        