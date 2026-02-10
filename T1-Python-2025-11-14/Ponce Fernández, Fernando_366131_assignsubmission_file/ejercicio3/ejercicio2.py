
def leer_ventas_tapas():
    datos =[]

    for i in range(4):
        nombre_tapa = input("Nombre de la tapa")
        precio_unitario = float(input("Dime el precio unitario"))
        cantidad_vendida = int(input("Dime la cantidad"))

    datos.append((nombre_tapa,precio_unitario,cantidad_vendida))
    
    return datos

def calcular_estadisticas_tapa(lista_ventas):

    dic =  {}
    
    for i in lista_ventas:

        key = i[0]
        valor1 = i[1]*i[2]
        valor2 = i[1]+(10*100)
        valor3 = i[2]
        if valor3>25:
            valor3 = "Alta"
        elif valor3>15:
            valor3 = "Media"
        else:
            valor3 = "Baja"

        dic[key]=(valor1,valor2,valor3)
        
    return dic
        

def analizar_rendimiento_tapas(dic):

    demanda = filter(lambda item: item[0][2] == "Alta", dic.items())
    tupla = tuple(map(lambda item: item[0][2], demanda))
    
    return list(tupla)
def main():
    datos = leer_ventas_tapas()
    print(datos)
    
    dic = calcular_estadisticas_tapa(datos)
    print(dic)

    print(analizar_rendimiento_tapas(dic))
    
if __name__ == "__main__":
    main()