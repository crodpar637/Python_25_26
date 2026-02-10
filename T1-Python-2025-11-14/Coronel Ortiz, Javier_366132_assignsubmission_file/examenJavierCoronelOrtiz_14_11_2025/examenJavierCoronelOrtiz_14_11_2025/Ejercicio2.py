from functools import reduce

def leer_ventas_tapas():
    lista_tapas = []

    for i in range(0,4):
        nombre_tapa = input("Nombre de la tapa: ")
        precio_unitario = float(input("Precio de la tapa: "))
        cantidad_vendida = int(input("Cantidad de ventas de la tapa: "))

        lista_tapas.append((nombre_tapa, precio_unitario, cantidad_vendida))
    return lista_tapas


def calcular_estadisticas_tapas(lista_ventas):
    diccionario_tapas = {}
    for tapa in lista_ventas:
        total = tapa[1]*tapa[2]
        diccionario_tapas[tapa[0]] = (total, total*0.1,"Alta" if (tapa[2] >= 25) else "Media" if (tapa[2]>15) else "Baja")
    return diccionario_tapas

def analizar_rendimiento_tapas(dic_estadisticas):
    tapas_alta_popularidad = map(lambda a: (a[0][0], a[1][0]),filter(lambda a: a[1][2]=="Alta", dic_estadisticas.items()))
    
    promedio_iva = sum(map(lambda a: a[1][1], dic_estadisticas.items()))
    promedio_iva/=len(dic_estadisticas)
    tapa_top = reduce(lambda a, b: a[0][0] if a[1][1]>b[1][1] else b[0][0], dic_estadisticas.items())

    return (list(tapas_alta_popularidad), promedio_iva, tapa_top[0])


def main():
    tulpaOriginal = leer_ventas_tapas()
    print(tulpaOriginal)
    diccionario = calcular_estadisticas_tapas(tulpaOriginal)
    print(diccionario)
    tulpaFinal = analizar_rendimiento_tapas(diccionario)
    print(tulpaFinal)
    
    
if __name__ == "__main__":
    main()
    print("Hola")