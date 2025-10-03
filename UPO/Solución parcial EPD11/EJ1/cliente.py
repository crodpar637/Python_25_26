from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, nif, telefono):
        super().__init__(nombre, nif)
        self.__telefono = telefono

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre} -- NIF: {self.nif} - Teléfono: {self.__telefono}"