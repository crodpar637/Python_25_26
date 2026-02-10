def leer_tapas():
    l=[]
    for a in range(1,5):
        nombre=input("nombre tapa: ")
        precio=input("precio_unitario: ")
        cantidad=input("cantidad vendida")
        l.append(nombre)
        l.append(precio)
        l.append(cantidad)
    return[l]

def calcular_estadisticas_tapas(lista_ventas):
    d={}
    popularidad=""
    for a in lista_ventas:
        if a[2]>25:
            popularidad="Alta"
        elif a[2]>15:
            popularidad="Media"
        else:
            popularidad="Baja"
        d[a[0]]=((a[1]*a[2]),((a[1]*a[2])/100),popularidad)


def analizar_rendimiento_tapas(dicc_estadisticas):

    filtrado=dicc_estadisticas.filter(d,key=lambda item:d[item[1][2]]=="Alta":)
    promedio=filtrado.reduce(suma+=)
    
    return

def main():
    l=leer_tapas()
    print(f"{l}")

if __name__=="__main__":
    main()