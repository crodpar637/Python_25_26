def leer_ventas_tapas():
    list = []
    for i in range (0, 4):
        nombre_tapa = input("Nombre de la tapa")
        precio_unitario = float(input("Precio por unidad"))
        cantidad_vendida = int(input("Cantidad vendida"))
        tup = (nombre_tapa, precio_unitario, cantidad_vendida)
        list.append(tup)
    return list

def calcular_estadisticas_tapas(lista_ventas):
    d = {}
    for tapa in lista_ventas:
        nombre_tapa = tapa[0]
        if tapa[2] > 25:
            popularidad = "Alta"
        else:
            if tapa[2] > 15:
                popularidad = "Media"
            else:
                popularidad = "Baja"
        t = (tapa[1]*tapa[2], tapa[1]*tapa[2]*0.1, popularidad)
        d[nombre_tapa] = t
    return d
    
def analizar_rendimiento_tapas(dic_estadisticas):
    tapas_alta_popularidad = [tapa[0:1] for tapa in dic_estadisticas if tapa[2] == "Alta"]
    promedio_iva = 0
    promedio_iva += [float(tapa.values()[1]) for tapa in dic_estadisticas] / 4
    tapa_top = max(tapa for tapa in dic_estadisticas)
    return (tapas_alta_popularidad, promedio_iva, tapa_top)

if __name__ == "__main__":
    a = leer_ventas_tapas()
    print(a)
    b = calcular_estadisticas_tapas(a)
    print(b)
    print(analizar_rendimiento_tapas(b))