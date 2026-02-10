def leer_ventas_tapas():
    lista_tapas = []

    for i in range(0,4):
        nombre_tapa = input("Dime el nombre de la tapa: ")
        precio_unitario = float(input("Dime el precio unitario de la tapa: "))
        cantidad_vendida = float(input("Dime la cantidad vendida de: " + nombre_tapa))
        lista_tapas.append( (nombre_tapa, precio_unitario, cantidad_vendida) )
        

    return lista_tapas

def calcular_estadisticas_tapa(lista_ventas):
    d = {}
    
    for venta in lista_ventas:
        

def main():
    print(leer_ventas_tapas())

main()