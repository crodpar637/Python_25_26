def main():

    def cargar_datos_csv():
        ruta_csv = "reservas.csv"
        lista_reservas_anyadir = []
    
        file=open(ruta_csv, "r")
        linea=file.readline()
        while True:
            linea=file.readline()
            if not linea:
                break
            lista_datos = linea.split(",")

        
            lista_reservas_anyadir.append((str(lista_datos[0]), lista_datos[1],str(lista_datos[2]), str(lista_datos[3]),str(lista_datos[4]))) 
    
        file.close()
    
        return (lista_reservas_anyadir)



    print(cargar_datos_csv())
    









main()