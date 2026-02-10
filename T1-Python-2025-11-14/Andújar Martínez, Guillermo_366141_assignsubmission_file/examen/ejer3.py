import csv
import pymysql

nombre_archivo = "reservas.csv"
#leemos y metemos en diccionario de diccionarios(ejer1)
dic = {}
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # Saltar la cabecera
    for fila in lector:
        id_reserva = fila[0]
        dic[id_reserva] = {
            "nombre": fila[1],
            "telefono": fila[2],
            "fecha": fila[3],
            "personas": fila[4],
            "mesa": fila[5]
        }

print("diccionario de diccionarios:", dic)

connection = pymysql.connect(
    host="db",      
    user="root",
    password="test",
    database="examen",
    port=3306
)
cursor = connection.cursor()

# Insertamos(ejer2)
for id_reserva, datos in dic.items():
    fila = (id_reserva, datos["nombre"], datos["telefono"], datos["fecha"], datos["personas"], datos["mesa"])
    cursor.execute("INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES (%s, %s, %s, %s, %s, %s)", fila)

connection.commit()

# fechas(ejer3)
def mostrar_reservas_fecha(fecha):
    cursor.execute("SELECT * FROM reserva WHERE fecha_reserva = %s", (fecha,))
    resultados = cursor.fetchall()
    print("Reservas para esta fecha:", resultados)

mostrar_reservas_fecha("2025-11-14")

cursor.close()
connection.close()
