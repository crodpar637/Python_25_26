from functools import reduce 

def entrada_datos():
    l = []

    for i in range(1,4):
        nombre = input("Nombre del equipo" + str(i) +  ":")
        puntos_favor = int(input("Puntos a favor del equipo"+ str(i) +  ":"))
        puntos_contra = int(input("Puntos en contra del equipo"+ str(i) + ":"))
        partidos = int(input("Número de partidos del equipo"+ str(i) +  ":"))

        l.append( ( nombre, puntos_favor, puntos_contra, partidos) )

    print(l)

    return l

def calculo_estadisticas(lista_datos):
    d = {}
    
    for equipo in lista_datos:
        diferencia = equipo[1] - equipo[2]
        tasa = diferencia / equipo[3]

        d[equipo[0]] = ( diferencia, tasa )

    return d

def extremos(dicc_datos):
    #{'betis': (20, 6.666666666666667), 'sevilla': (-850, -283.3333333333333), 'rayo': (33, 11.0)}

    equipo_max_diferencia = reduce(lambda item1, item2: item1 if item1[1][0] > item2[1][0] else item2, dicc_datos.items())
    equipo_menor_diferencia = reduce(lambda item1, item2: item1 if item1[1][0] < item2[1][0] else item2, dicc_datos.items())

    return [ equipo_max_diferencia[0] , equipo_menor_diferencia[0] ]
  
def guardar_datos(dicc_datos):
    #{'betis': (20, 6.666666666666667), 'sevilla': (-850, -283.3333333333333), 'rayo': (33, 11.0)}

    f = open("baloncesto.csv","wt")

    for (k,v) in dicc_datos.items():
        f.write(k + ',' + str(v[0]) + ',' + str(v[1]) + '\n')

    f.close()
    
def main():
    l = entrada_datos()
    # l = [('betis', 100, 80, 3), ('sevilla', 40, 890, 3), ('rayo', 56, 23, 3)]
    dicc_datos_estadistica = calculo_estadisticas(l) 
    print(dicc_datos_estadistica)
    print(extremos(dicc_datos_estadistica))
    guardar_datos(dicc_datos_estadistica)
    
    
if __name__ == "__main__":
    main()

   
    
                           

