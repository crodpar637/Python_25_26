from functools import reduce

def leer_ventas_tapas():
    tapas = []
    for i in range(4):
        nombre_tapa = input("Dime el nombre de la tapa")
        precio_unitario = float(input("Dime el precio de cada unidad"))
        cantidad_vendida = int(input("Dime la cantidad vendida"))
        tapas.append((nombre_tapa, precio_unitario, cantidad_vendida))

    return(tapas)


def calcular_estadisticas_tapas(lista_ventas):

    estadisticas = {}
    for i in lista_ventas:
        if i[2]> 25:
            popularidad = "Alta"
        elif i[2] <=15:
            popularidad = "Baja"
        else:
            popularidad = "Media"
        estadisticas[i[0]] = (i[1]*i[2], i[1]*i[2]*0.1,popularidad)
        
    return estadisticas

def analizar_rendimiento_tapas(dic_estadisticas):
    tapas_alta_popularidad = list(filter(lambda item: item[1][2] == "Alta", dic_estadisticas.items()))
    tapa_top = reduce(lambda it1, it2 : it1 if it1[1][0] > it2[1][0] else it2, dic_estadisticas.items())[0]
    return (tapas_alta_popularidad, tapa_top)
    
if __name__=="__main__":
    ventas = leer_ventas_tapas()
    print(ventas)
    estadisticas = calcular_estadisticas_tapas(ventas)
    print(estadisticas)
    print(analizar_rendimiento_tapas(estadisticas))
    