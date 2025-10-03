class Pedido:
    def __init__(self, cliente, platos):
        self.__cliente = cliente
        self.__platos = platos

    def calcular_total(self, precios):
        total = 0
        for plato in self.__platos:
            if plato in precios:
                total += precios[plato]
        return total

    def __str__(self):
        return f"Pedido de {self.__cliente.nombre}: {self.__platos}"