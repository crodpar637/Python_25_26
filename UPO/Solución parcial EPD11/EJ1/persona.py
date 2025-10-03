class Persona:
    def __init__(self, nombre, nif):
        self.__nombre = nombre
        self.__nif = nif

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nif(self):
        return self.__nif

    @nif.setter
    def nif(self, nif):
        self.__nif = nif

    def __str__(self):
        return f"Nombre: {self.__nombre} -- NIF: {self.__nif}"