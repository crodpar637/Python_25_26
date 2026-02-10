def cargar_reservas_desde_csv():
    f = open("../reservas.csv", "r", encoding="utf-8")
    lineas = f.readlines()
    f.close()
    
    lista_campos = lineas[0].strip().split(",")
    print("cabecera:", lista_campos)
    
    d={}
    d2={}
    for linea in lineas:
        campos = linea.strip().split(",")
        d["nombre"]=campos[1]
        d["telefono"]=campos[2]
        d["fecha"]=campos[3]
        d["personas"]=campos[4]
        d["mesa"]=campos[5]
        
        d2[campos[0]]= d
        
    print(list(d2))


cargar_reservas_desde_csv()