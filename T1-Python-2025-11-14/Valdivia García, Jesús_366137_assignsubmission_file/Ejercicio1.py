class Empleado():
    def __init__(self,nombre,salario_base):
        self._nombre = nombre
        self._salario_base = salario_base

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor

    @property
    def salario_base(self):
        return self._salario_base
    @salario_base.setter
    def salario_base(self,valor):
        self._salario_base = valor

    def calcular_salario(self,irpf):
        calcular_salario = self.salario_base - ( self.salario_base*(irpf/100))
        self.salario_base = calcular_salario
        return(str(calcular_salario))

    def __str__(self):
        return("Nombre: " + self.nombre + ", Salario base: " + str(self.salario_base))


class Vendedor(Empleado):
    def __init__(self,nombre,salario_base, ventas_realizadas):
        Empleado.__init__(self,nombre,salario_base)
        self._ventas_realizadas = ventas_realizadas

    @property
    def ventas_realizadas(self):
        return self._ventas_realizadas

    def calcular_salario(self):
        cont_dinero = 0
        for dinero in self.ventas_realizadas:
            cont_dinero += dinero
        dinero_final = self.salario_base + (cont_dinero * (10/100))
        return(str(dinero_final))

    def agregar_venta(self,importe):
        self.ventas_realizadas.append(importe)
        
    
    
        
    def __str__(self):
        return("Nombre: "+ self.nombre + ", Salario base: " + str(self.salario_base) + ", Ventas: " + str(self._ventas_realizadas) + ", Salario total: " + self.calcular_salario())
    
        
def main():

    jesus = Empleado("Jesus",1000)
    manuel = Empleado("Manuel" , 2000)
    print(jesus)
    print(manuel)
    jesus.calcular_salario(15)
    print(jesus)
    print(manuel)
    

    iker = Vendedor("Iker",1000,[100,200,200])
    herme = Vendedor("Herme",250 , [200,350,500])
    print(iker)
    print(herme)
    iker.calcular_salario()
    iker.agregar_venta(50)
    iker.agregar_venta(1200)
    print(iker)
    print(herme)
   



main()

    