from cliente import Cliente
from pedido import Pedido

# Crear clientes
cliente1 = Cliente("Juan Pérez", "12345678A", "600123456")
cliente2 = Cliente("Ana Gómez", "87654321B", "600654321")

# Crear pedidos
pedido1 = Pedido(cliente1, ["serranito", "croquetas"])
pedido2 = Pedido(cliente2, ["ensalada", "torrija"])

# Diccionario de precios
precios = {
    'serranito': 5.50,
    'croquetas': 3.75,
    'ensalada': 4.25,
    'torrija': 3.00
}

# Mostrar información de los pedidos
print(pedido1)
print(pedido2)

# Calcular y mostrar los totales de cada pedido
print(f"Total del pedido 1: {pedido1.calcular_total(precios)}€")
print(f"Total del pedido 2: {pedido2.calcular_total(precios)}€")