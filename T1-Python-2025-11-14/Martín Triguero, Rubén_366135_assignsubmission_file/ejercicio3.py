import pymysql

#Conexion con la base de datos

    

def cargar_reservas_desde_csv():
    ruta_csv = "reservas.csv"
    diccionario = {}
    
    file=open(ruta_csv, "r")
    linea=file.readline()
    while True:
        linea=file.readline()
        if not linea:
            break
        lista_datos = linea.split(",")
        diccionario

        #formato de linea: 101,David Ruiz,Ventas,35000.0
        diccionario[int(lista_datos[0])] = {"nombre": lista_datos[1],"telefono": str(lista_datos[2]),"fecha": str(lista_datos[3]),"personas": int(lista_datos[4]),"mesa": int(lista_datos[5])} 
    
    file.close()
    return diccionario

def insertar_reservas_bbdd(reservas):
    connection = pymysql.connect(
        host="db",      # IP del host Docker
        user="root",
        password="test",
        database="examen",
        port=3306
    )
    cursor = connection.cursor()
    
    for reserva in reservas.items():
        id_reserva = reserva[0]
        nombre = reserva[1].get("nombre")
        telefono = reserva[1].get("telefono")
        fecha = reserva[1].get("fecha")
        personas = reserva[1].get("personas")
        mesa = reserva[1].get("mesa")

        # INSERT INTO jugadores (nombre, puntos_favor, puntos_contra, partidos)
        # VALUES (%s, %s, %s, %s)
        # """
        # cursor.execute(sql_insert, ("Carlos", 25, 18, 5))
        
        sql = f"""INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa) 
        VALUES ({id_reserva}, '{nombre}', '{telefono}', '{fecha}', {personas}, {mesa});"""
        print("Insertando " + str(reserva))
        cursor.execute(sql)
        
    connection.commit()
    connection.close() # cerramos la conexión si no vamos a trabajar más con la bbdd


def mostrar_reservas_fecha(fecha):
    connection = pymysql.connect(
        host="db",      # IP del host Docker
        user="root",
        password="test",
        database="examen",
        port=3306
    )
    cursor = connection.cursor()
    sql = f"""SELECT * FROM reserva 
    WHERE fecha_reserva = {fecha} ;"""
    
    cursor.execute(sql)

    # Obtengo todas las filas que devuelve la consulta
    rows = cursor.fetchall()
    
    # Cerrar conexion    
    connection.close() # cerramos la conexión si no vamos a trabajar más con la bbdd
    for r in rows:
        print(r)

if __name__ == "__main__":
    print(cargar_reservas_desde_csv())

    insertar_reservas_bbdd(cargar_reservas_desde_csv())
    mostrar_reservas_fecha('2025-03-15')
    












