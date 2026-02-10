import pymysql
import csv

connection = pymysql.connect(
    host="db",
    user="root",
    password="test",
    database="examen",
    port=3306
)
cursor = connection.cursor()

def cargar_reservas_desde_csv():
    reservas = []
    with open("reservas.csv", mode='r', newline='', encoding='utf-8') as file_csv:
        reader_dict = csv.DictReader(file_csv)
        for fila in reader_dict:
            reservas.append(fila)
    return reservas

def insertar_reservas_bbdd(reservas):
    for fila in reservas:
        sql = f"INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES ({fila['id']}, '{fila['nombre']}', {fila['telefono']}, '{fila['fecha']}', {fila['personas']}, {fila['mesa']})"
        cursor.execute(sql)
    connection.commit()

x = cargar_reservas_desde_csv()
print(x)
insertar_reservas_bbdd(x)