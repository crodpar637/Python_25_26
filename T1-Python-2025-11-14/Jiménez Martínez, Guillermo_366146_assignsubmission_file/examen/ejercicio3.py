import csv

import pymysql

connection = pymysql.connect(
    host="db",     
    user="root",
    password="test",
    database="examen",
    port=3306
)

def cargar_reservas_desde_csv():

    with open("reservas.csv", newline='') as f:
        data = csv.reader(f, delimiter = ',')
        next(data)

        d = {}
        
        for fila in data:
            d_valores = {}
            
            id = int(fila[0])
            nombre = fila[1]
            telefono = int(fila[2])
            fecha = fila[3]
            personas = int(fila[4])
            mesa = int(fila[5])

            d_valores['nombre'] = nombre
            d_valores['telefono'] = telefono
            d_valores['fecha'] = fecha
            d_valores['personas'] = personas
            d_valores['mesa'] = mesa
            
            d[id] = (d_valores)


    return(d)

def insertar_reservas_bbdd(reservas):
    cursor = connection.cursor()
    
    sql = "INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES (%s,%s,%s,%s,%s,%s)"

    for fila in reservas.keys:
        id = fila
        for i in reservas[fila].keys:
            nombre = i[id][0]
            telefono = i[id][1]
            fecha = i[id][2]
            personas = i[id][3]
            mesa = i[id][4]
            #cursor.execute('"INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES ('id + ', ' + nombre + ', ' + telefono + ', ' + fecha + ', ' + personas + ', ' + mesa')')
        
        

def main():
    print(cargar_reservas_desde_csv())

    insertar_reservas_bbdd(cargar_reservas_desde_csv())

main()