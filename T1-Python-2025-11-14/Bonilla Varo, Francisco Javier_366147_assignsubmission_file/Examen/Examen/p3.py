import csv
import pymysql

def cargar_reservas_desde_csv():
    dicc = {}
    with open("reservas.csv", "r", newline = "", encoding="utf-8") as f:
        #Leemos todos las lineas del fichero
        reader = csv.reader(f)
        next(reader)
        for fila in reader: 
            dicc[fila[0]] = ("nombre: "== fila[1]), ("telefono: "== fila[2]), ("fecha: "== fila[3]), ("personas: "== fila[4]), ("mesa: " == fila[5])
            return dicc

def insertar_reservas_bbdd(reservas):
    cursor = db_conn.cursor()
    # Realizamos el insert en las filas
    sql = "INSERT INTO Reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) VALUES (:id, :nombre_cliente, :telefono, :fecha_reserva, :numero_personas, :numero_mesa)"
    
    """ Ejecutamos el insert en bloque utilizando ejecutemany() para insertar múltiples registros a la vez. """
    cursor.executemany(sql, lista_empleados)
    db_conn.commit()  # Confirmamos los cambios en la base de datos


    connection = pymysql.connect(
        host="db",   # Cambia según tu configuración
        user="root",
        password="test",   # Cambia por tu contraseña
        database="examen",
        port=3306
    )


def main():

    print(cargar_reservas_desde_csv())

    
    insertar_reservas_bbdd("reservas.csv")
    conn.close()
main()