from functools import reduce


def main():

    #a
    lista_tapas= []
    def leer_ventas_tapas():
        for i in range (0,4):
            nombre = input("Dime el nombre de la tapa")
            precio_unitario = input("¿Cuanto cuesta?")
            cantidad_vendida = input("¿Cuantas unidades se han vendido?")
            lista_tapas.append((nombre , str(precio_unitario) , str(cantidad_vendida)))
        print(lista_tapas)

    #b
    lista_ventas = [('Serranito',3.5,25), ('Solimillo al Whisky',4.2,18),('Montadito de pringá',2.8,32),('Espinacas con garbanzos',3.0,21)]
    d = {}
    def calcular_estadisticas_tapas(lista_ventas):
        for tapa in lista_ventas:
            suma = 0
            suma = tapa[1]*tapa[2]
            iva = suma*(10/100)
            popularidad = ""
            if tapa[2] <= 15:
                popularidad = "Baja"
            elif tapa[2] > 25:
                popularidad = "Alta"
            else:
                popularidad = "Media"
                
            d[tapa[0]] = (str(suma) , str(iva),popularidad)
        return d
            

    #{'Serranito': ('87.5', '8.75', 'Media'), 'Solimillo al Whisky': ('75.60000000000001', '7.560000000000001', 'Media'), 'Montadito de pringá': ('89.6', '8.959999999999999', 'Alta'), 'Espinacas con garbanzos': ('63.0', '6.300000000000001', 'Media')}
    #c
    def analizar_rendimiento_tapas(diccionario):
        l = []
        tapas_alta = filter(lambda i : i[1][2] == "Alta", diccionario.items())
        tapa_top = reduce(lambda t1 , t2 :t1 if t1[1][0] > t2 [1][0] else t2 ,diccionario.items())
        l.append(list(tapas_alta))
        l.append(tapa_top[0])
        print(l)
        


    
    
    #leer_ventas_tapas()
    print(calcular_estadisticas_tapas(lista_ventas))
    analizar_rendimiento_tapas(calcular_estadisticas_tapas(lista_ventas))





main()


    