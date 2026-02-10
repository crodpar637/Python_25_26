def leer_ventas_tapas():
    tapas = []
    for i in range(0,4):
        nombre_tapa = input("Introduce nombre de la tapa:")
        precio_unitario = float(input("Introduce precio unitario:"))
        cantidad_vendida = int(input("Introduce cantidad vendida:"))
        tapas.append((nombre_tapa,precio_unitario,cantidad_vendida))

    return print(tapas)


def calcular_estadisticas_tapas(lista_ventas):
    estadisticas = {}
    for venta in lista_ventas:
        nombre_tapa = venta[0]
        total_ventas = venta[1] * venta[2]
        iva = total_ventas * 10 / 100
        popularidad = ''
        if venta[2] >= 25:
            popularidad = 'Alta'
        elif venta[2] > 15:
            popularidad = 'Media'
        else:
            popularidad = 'Baja'
        estadisticas[nombre_tapa] = (total_ventas, iva, popularidad)

    return print(estadisticas)

def analizar_rendimiento_tapas(dic_estadisticas):
    popularidad_alta = list

def main():
    #apartadoA = leer_ventas_tapas()
    listado_apartadoB = [
        ('Serranito', 3.5, 25),
        ('Solomillo al whisky', 4.2, 18),
        ('Montadito de pringá', 2.8, 32),
        ('Espinacas con garbanzos', 3.0, 21)
    ]
    apartadoB = calcular_estadisticas_tapas(listado_apartadoB)
    diccionario_apartadoC = {
        'Serranito': (87.5, 8.75, 'Alta'),
        'Solomillo al whisky': (75.60000000000001, 7.560000000000001, 'Media'),
        'Montadito de pringá': (89.6, 8.96, 'Alta'),
        'Espinacas con garbanzos': (63.0, 6.3, 'Media')
    }

    apartadoC = analizar_rendimiento_tapas(diccionario_apartadoC)
    






if __name__ == "__main__":
    main()