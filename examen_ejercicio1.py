class Usuario():

    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self,valor):
        self.__direccion = valor


    def __str__(self):
        return "Nombre: " + self.__nombre + " Direccion: " + self.__direccion

class Monitor(Usuario):

    def __init__(self,nombre, direccion, identificador):
        super().__init__(nombre, direccion)
        self.__identificador = identificador

    
    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self,valor):
        self.__identificador = valor

    def __str__(self):
        return super().__str__() + " Identificador: "  + str(self.__identificador)

if __name__ == "__main__":
    u = Usuario("Pepe", "El Bar")
    u.direccion = "El restaurante"
    print(u)
    m = Monitor("Jose", "Mercadona", 22)
    print(m)
    