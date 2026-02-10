from functools import reduce
def leer_ventas_tapas():
    l=[]
    nombre=""
    precio=0
    cantidad_ventas=0
    for i in range(4):
        nombre = input("Pon el nombre de la tapa: ")
        precio= input("Precio unitario: ")
        cantidad_ventas=input("Pon la cantidad de ventas")
        t=(nombre,float(precio),int(cantidad_ventas))
        l.append(t)
    return l

#[('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringa', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]
def calcular_estadisticas_tapas(lista_ventas):
    d={}
    total_ventas=0
    iva_aplicado=0
    popularidad=""
    for tapa in lista_ventas:
        total_ventas=tapa[1]*tapa[2]
        iva_aplicado=total_ventas/10
        
        if tapa[2]>25:
            popularidad="Alta"
        elif tapa[2]>15:
            popularidad="Media"
        elif tapa[2]<=15:
            popularidad="Baja"

        t=(total_ventas,iva_aplicado,popularidad)
        d[str(tapa[0])]=t
    return d


#{'Serranito':(87.5, 8.75, 'Media'),'Solomillo al whisky':(75.60000000000001, 7.5600000000000005, 'Media'),'Montadito de pringa':(89.6, 8.959999999999999, #'Alta'),'Espinacas con garbanzos':(63.0, 6.3, 'Media')}
def analizar_rendimiento_tapas(dic_estadisticas):
    #{'Montadito de pringa':(89.6, 8.959999999999999, 'Alta')}
    altas_popularidad_alta=filter(lambda item: item[1][2] == "Alta",dic_estadisticas.items())
    total_iva = reduce(lambda item1, item2: item1 + item2[1], dic_estadisticas.values(), 0)
    cont=0
    for i in dic_estadisticas.keys():
        cont +=1
    promedio_iva = total_iva/cont
    
    mayor=0
    """
    mayor_recaudacion = filter(lambda item: item[1][0]>mayor ,dic_estadisticas.values())
    print(list(mayor_recaudacion))"""
    t=(list(altas_popularidad_alta),promedio_iva,)
    return t



#print(leer_ventas_tapas())
l1=[('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringa', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]
d1 = calcular_estadisticas_tapas(l1)

d2 = {'Serranito':(87.5, 8.75, 'Media'),
      'Solomillo al whisky':(75.60000000000001, 7.5600000000000005, 'Media'),
      'Montadito de pringa':(89.6, 8.959999999999999, 'Alta'),
      'Espinacas con garbanzos':(63.0, 6.3, 'Media')}


"""for clave, valor in d2.items():
    print(f"'{clave}':{valor}")"""

print(list(analizar_rendimiento_tapas(d2)))




