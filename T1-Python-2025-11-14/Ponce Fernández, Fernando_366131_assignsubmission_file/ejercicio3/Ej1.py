class Empleado:
    
    def __init__(self,nombre,salario_base):
        self.__nombre = nombre
        self.__salario_base = salario_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salario_base(self):
        return self.__salario_base

    @nombre.setter
    def nombre(self,valor):
        if not valor:
            raise ValueError("Nombre no puede estar vacio")
        self.__nombre = nombre


    @salario_base.setter
    def salario_base(self,valor):
        if not valor:
            raise ValueError("salario_base no puede estar vacio")
        self.__salario_base = salario_base

    def calcular_salario(irpf):

        return self.__salario_base - (irpf/100)

   
     
    def __str__(self):

        return f"{self.__class__.__name__}(nombre ={self.__nombre},Salario_base='{self.__salario_base})"

    def info(self):
        return f"{self.__class__.__name__}(nombre ={self.__nombre},Salario_base='{self.__salario_base})"
        
class Vendedor(Empleado):

    def __init__(self,nombre,salario_base,ventas_realizadas):
        self.__ventas_realizadas =[]

    @property
    def ventas_realizadas(self):
        return self.__ventas_realizadas

    def calcular_salario(self,salario_base):

        sumaDeVentas =0
        for v in self.__ventas_realizadas:
            sumaDeVentas+=v

        return sumaDeVentas-(salario_base/100)
    

    def agregar_venta(importe):

        return ventas_realizadas.append(importe)

    def __srt__(self):
        return f"{super().__str__()},Ventas_realizadas ={self.__ventas_realizadas}"
        
    def info(self):
        return f"{super().__str__()},Ventas_realizadas ={self.__ventas_realizadas}"

def main():


if __name__ == "__main__":
    main()
        