from functools import reduce

def leer_ventas_tapas():
    l = []
    for n in range(0,4):
        nombre_tapa = input("Nombre de la tapa: ")
        precio_unitario = float(input("Precio unitario: "))
        cantidad_vendida = int(input("Unidades vendidas: "))
        l.append((nombre_tapa,precio_unitario,cantidad_vendida))
    return l
    
def calcular_estadisticas_tapas(lista_ventas):
    d = {}
    for t in lista_ventas:
        total_ventas = t[1] * t[2]
        
        iva_aplicado = 10*total_ventas/100

        popularidad = ""
        if t[2] >= 25:
            popularidad = "Alta"
        elif t[2]>15:
            popularidad = "Media"
        elif t[2] <= 15:
            popularidad = "Baja"
        
        d[t[0]] = (total_ventas,iva_aplicado,popularidad)
    return d

def analizar_rendimineto_tapas(dic_estadisticas):
    tupla = ()
    popularidadAlta = filter(lambda item :item[1][2] == "Alta",dic_estadisticas.items())
    #totalIVA = reduce(lambda item1, item2: item1[1][1] + item2[1][1],dic_estadisticas.items())
    #promedioIVA = totalIVA / 4
    mayRec = reduce(lambda item1, item2: item1 if item1[1][0] > item2[1][0] else item2,dic_estadisticas.items())
    return tupla[popularidadAlta,0,mayRec[0]]

def main():
    lista = leer_ventas_tapas()
    print(lista)

    diccionario = calcular_estadisticas_tapas(lista)
    print(diccionario)

    rendimiento = analizar_rendimineto_tapas(diccionario)
    print(rendimiento)

main()


        
        