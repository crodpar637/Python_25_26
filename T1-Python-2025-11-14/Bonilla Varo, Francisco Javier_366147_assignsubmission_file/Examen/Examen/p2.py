def leer_ventas_tapas():
    tapas = []
    for tapa in range(0,4):
        nombre_tapa = input("Nombre de la tapa: ")
        precio_unitario = float(input("Precio unitario: "))
        cantidad_vendida = int(input("Cantidad individual: "))
        tapas.append((nombre_tapa, precio_unitario, cantidad_vendida))
    print(tapas)
    return tapas

def calcular_estadisticas_tapas(lista_ventas):
    
    estadisticas = {}

    for lista in lista_ventas:
        #nombre          precio_unitario  cantidad
        # lista_ventas[0], lista_ventas[1], lista_ventas[2]

        precio_unitario = lista[1]
        cantidad = lista[2]
        total_ventas = precio_unitario * cantidad

        iva_aplicado =  (total_ventas * 10 / 100)
        if lista[2] > 25:
            popularidad = "Baja"
        elif lista[2] > 15:
            popularidad = "Media"
        else:
            popularidad = "Baja"

        estadisticas[lista[0]] = (total_ventas, iva_aplicado, popularidad)
    print(estadisticas)
    return estadisticas

# def analizar_rendimiento_tapas(dic_estadisticas):
    

def main():
    leer_ventas_tapas()

    lista_ventas = [
        ("Serranito", 3.5, 25),
        ("Solomillo al whisky", 4.2, 18),
        ("Montadito de pringa", 2.8, 32),
        ("Espinacas con garbanzos", 3.0, 21)
    ]
    
    calcular_estadisticas_tapas(lista_ventas)

    lista_ventas = [
        {"nombre_tapa" : "Serranito", "precio_unitario" : 3.5, "cantidad_individual" : 25},
        {"nombre_tapa" : "Solomillo al whisky", "precio_unitario" : 4.2, "cantidad_individual" : 18},
        {"nombre_tapa" : "Montadito de pringa", "precio_unitario" : 2.8, "cantidad_individual" : 32},
        {"nombre_tapa" : "Espinacas con garbanzos", "precio_unitario" : 3.0, "cantidad_individual" : 21}

    ]
    
    analizar_rendimiento_tapas()

main()