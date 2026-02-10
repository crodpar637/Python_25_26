import csv
import pymysql

def cargar_reservas_desde_csv():
    dict={}
    with open("reservas.csv", newline="", encoding="utf-8") as f:
        reader=csv.reader(f)
        next(reader)
        for fila in reader:
            dict[fila[0]] = {"Nombre": fila[1], "Teléfono":fila[2], "Fecha":fila[3], "Personas":int(fila[4]), "Mesa":int(fila[5])}
        return dict

def insertar_reservas_bbdd(reservas):
    conexion = pymysql.connect(
     host="db",          
     user="root",        
     password="test",  
     database="examen",     
     charset="utf8mb4",         
     cursorclass=pymysql.cursors.DictCursor  
     )
    cursor = conexion.cursor()

    sql_insert = """
     INSERT INTO reserva (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa)
     VALUES (%s, %s, %s, %s, %s, %s)
     """
    for i in reservas:
        id = i.getKey()
        valores = id.getValue().values()
        cursor.execute(sql_insert, (id, valores[0],valores[1],valores[2],valores[3],valores[4]))
    conexion.commit()
    cursor.close()
    conexion.close()
    
def mostrar_reservas_fecha(fecha):
    conexion = pymysql.connect(
     host="db",          
     user="root",        
     password="test",  
     database="examen",     
     charset="utf8mb4",         
     cursorclass=pymysql.cursors.DictCursor  
     )
    cursor = conexion.cursor()
    sql_select = """
 SELECT nombre_cliente, telefono, numero_personas, numero_mesa
 FROM reserva
 WHERE fecha_reserva = %s
 """
    cursor.execute(sql_select, fecha)

    resultados = cursor.fetchall()
    totalComensales=0
    print("RESERVAS PARA "+fecha)
    print("=" * 21)
    for fila in resultados:
        print("Mesa "+fila[3]+": "+fila[0]+" ("+fila[2]+" personas) - Tel: "+fila[1])
        totalComensales+=fila[2]
    print("Total "+len(fila)+", "+totalComensales+" personas")
    cursor.close()
    conexion.close()

if __name__=="__main__":
    reservas=cargar_reservas_desde_csv()
    print(reservas)
    # insertar_reservas_bbdd(reservas)
    mostrar_reservas_fecha('2025-03-15')
    mostrar_reservas_fecha('2025-11-14')