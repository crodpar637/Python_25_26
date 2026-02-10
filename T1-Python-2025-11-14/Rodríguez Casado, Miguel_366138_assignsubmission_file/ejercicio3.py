import pymysql
import csv 


def cargar_reservas_desde_csv():
    
    with open("reservas.csv", "r", newline="",encoding = "utf-8") as file:
        reader = csv.reader(file)
        d = {}
        next(reader) #esto salta la primera linea q es la cabecera
        for fila in reader:
            d[fila[0]] = {"nombre": fila[1], "telefono": fila[2], "fecha":fila[3], "personas": fila[4], "mesa": fila[5]}

    return d
        
def insertar_reservas_bbdd(reservas):
    connection = pymysql.connect(
    host="db",      # IP del host Docker
    user="root",
    password="test",
    database="examen",   #nombre de la base de datos
    port=3306
    )
    cursor = connection.cursor()

    for items in reservas.value():
        cursor.execute("INSERT INTO reserva  VALUES (%s)", fila)
        
    connection.commit()
    cursor.close()
    connection.close()
    
def main():
    d = cargar_reservas_desde_csv()
    print(d)
   

main()