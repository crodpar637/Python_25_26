l=[]
def leer_ventas_tapas():
    for i in range(4):
        nombre_tapa = input("Nombre de la tapa:")
        precio_unitario = float(input("Precio de la tapa:"))
        cantidad_vendida = int(input("Cantidad vendida:"))

        l.append( ( nombre_tapa, precio_unitario, cantidad_vendida) )

    print(l)

    return l

def calcular_estadisticas_tapas(lista_ventas):
    dic={}
    for venta in lista_ventas:
        nombre = venta[0]
        total_ventas = venta[1]*venta[2]
        iva_aplicado = total_ventas*0.1
        if venta[2]>25:
            popularidad = "Alta"
        elif venta[2]>=15:
            popularidad = "Media"
        else:
            popularidad = "Baja"
            
        dic[nombre] = (total_ventas, iva_aplicado, popularidad)

    print(dic)

#def analizar_rendimiento_tapas(dic): no me dio tiempo a hacerlo, me estanqué y decidí borrarlo y pasar al ejer3 mejor.
    

# Programa principal
if __name__ == "__main__":
    leer_ventas_tapas()
    calcular_estadisticas_tapas(l)