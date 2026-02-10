#a
def leer_ventas_tapas():
    listaTapas=list()
    for i in range(4):
        nombre_tapa=input("Introduzca el nombre de la tapa: ")
        precio_unitario=float(input("Introduzca el precio de la tapa: "))
        cantidad_vendida=int(input("Introduzca la cantidad de tapas vendidas: "))
        tapa=(nombre_tapa,precio_unitario,cantidad_vendida)
        listaTapas.append(tapa)
    return listaTapas

#b
def calcular_estadisticas_tapas(lista_ventas):
    diccionario=dict()
    for venta in lista_ventas:
        totVenta=venta[1]*float(venta[2])
        popularidad="Baja"
        if venta[2]>25:
            popularidad="Alta"
        elif venta[2]>15:
            popularidad="Media"
        diccionario[venta[0]]=(totVenta,totVenta*0.1,popularidad)
    return diccionario

#c
#def analizar_rendimiento_tapas(dic_estadisticas):
    


def main():
    print(leer_ventas_tapas())
    lista_ventas=[('Serranito', 5.5, 20000), ('Ensaladilla rusa', 3.0, 132), ('Montadito', 4.0, 300), ('Nosemas', 200.0, 1230)]
    print(calcular_estadisticas_tapas(lista_ventas))
    

    
if __name__=="__main__":
    main()