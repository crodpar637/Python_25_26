from functools import reduce

def leer_ventas_tapas():
    datos_tapas = []
    
    print("Introduce datos de 4 tapas típicas Sevillanas:")
    for i in range(4):
        print(f"Introduce los datos de la tapa {i+1}")
        nombre_tapa = input("Introduce el nombre de la tapa: ")
        precio_unitario = float(input("Introduce el precio unitario de la tapa: "))
        cantidad_vendida = int(input("Introduce la cantidad vendida de la tapa: "))
        
        datos_tapas.append((nombre_tapa, precio_unitario, cantidad_vendida))
        
    return datos_tapas

def calcular_estadisticas_tapas(lista_ventas):
    dic_ventas = {}
    
    for tapa in lista_ventas:
        nombre = tapa[0]
        precio_unitario = tapa[1]
        cantidad = tapa[2]

        total_ventas = precio_unitario*cantidad
        iva_aplicado = total_ventas*(10/100)
        popularidad = "Baja"
        if cantidad > 25: 
            popularidad = "Alta" 
        elif cantidad > 15: 
            popularidad = "Media"
        
        dic_ventas[nombre] = (total_ventas, iva_aplicado, popularidad)
        
    return dic_ventas

def analizar_rendimiento_tapas(dic_estadisticas):
    filtro_popularidad = filter(lambda item: item[1][2] == "Alta", dic_estadisticas.items())
    tapas_alta_popularidad = map(lambda item: (item[0], item[1][0]), filtro_popularidad)
    
    lista_iva = map(lambda x: x[1][1] ,dic_estadisticas.items())
    promedio_iva = sum(lista_iva)/len(dic_estadisticas)

    tapa_top = reduce(lambda x, y: x if x[1][0] > y[1][0] else y, dic_estadisticas.items())
    
    return (list(tapas_alta_popularidad), promedio_iva, tapa_top[0])

leer = leer_ventas_tapas()
calcular = calcular_estadisticas_tapas(leer)
analizar = analizar_rendimiento_tapas(calcular)

print(calcular)
print(analizar)