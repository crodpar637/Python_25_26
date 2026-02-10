from functools import reduce

def leer_ventas_tapas():
    lista_tapas=[]
    for numero_tapa in range(1,5):
        nombre_tapa = input("Introduce el nombre de la tapa:"+str(numero_tapa))
        precio_unitario = float(input("Introduce el precio unitario de la tapa:"+str(numero_tapa)))
        cantidad_vendida = int(input("Introduce la cantidad vendida de la tapa:"+str(numero_tapa)))
        lista_tapas.append((nombre_tapa, precio_unitario, cantidad_vendida))
    return lista_tapas

def calcular_estadisticas_tapas(lista_ventas):
    # [('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringa', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]
    dic_ventas = {}
    for tapa in lista_ventas:
        total_ventas = tapa[1] * tapa[2]
        iva_aplicado = total_ventas * 10 / 100
        popularidad = "Baja"
        if tapa[2] >= 25:
            popularidad = "Alta"
        elif tapa[2] >= 15:
            popularidad = "Media"

        dic_ventas[tapa[0]] = (total_ventas, iva_aplicado, popularidad)

    return dic_ventas

def analizar_rendimiento_tapas(dic_estadisticas):
    tapas_alta_popu = filter(lambda item: item[1][2] == "Alta" ,dic_estadisticas.items())
    print(list(tapas_alta_popu))
    suma_IVA = reduce(lambda item1, item2 : item1[1][1] + item2[1][1] ,dic_estadisticas.items(),0)
    print(list(suma_IVA))
    promedio_IVA = suma_IVA / len(dic_estadisticas.items())
    mayor_recau = reduce(lambda item1, item2 : item1 if item1[1][0] > item2[1][0] else item2 ,dic_estadisticas.items())
    print(mayor_recau)
    
    


#Ejecución del programa principal
if __name__ == "__main__":
    print(leer_ventas_tapas())
    #Formato devuelto: [('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringa', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]

    lista_tapas = [('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringa', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]
    print(calcular_estadisticas_tapas(lista_tapas))
    #Formato devuelto: {'Serranito': (87.5, 8.75, 'Alta'), 'Solomillo al whisky': (75.60000000000001, 7.560000000000001, 'Media'), 'Montadito de pringa': (89.6, 8.96, 'Alta'), 'Espinacas con garbanzos': (63.0, 6.3, 'Media')}
    dicc = {'Serranito': (87.5, 8.75, 'Alta'), 'Solomillo al whisky': (75.60000000000001, 7.560000000000001, 'Media'), 'Montadito de pringa': (89.6, 8.96, 'Alta'), 'Espinacas con garbanzos': (63.0, 6.3, 'Media')}
    
    #Sin terminar
    analizar_rendimiento_tapas(dicc)

    