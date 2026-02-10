import csv
import pymysql
import os

try:
    connection = pymysql.connect(
        host="db",    
        user="root",
        password="test",
        database="examen",
        port=3306,
        autocommit=True 
    )
    print("Conexion SQL realizada")
except pymysql.Error as e:
    print(f"Erro al conectar a la BD: {e}")
    exit()

def cargar_reservas_desde_cv(ruta_csv):
    datos_procesados = []
    try:
        with open(ruta_archivo, mode='r', encoding="utf-8") as f:
            fila_convertida = {
                'id' : fila[id],
                'nombre' : fila[nombre],
                'fecha' : fila[fecha],
                'personas' : fila[personas],
                'mesa' : fila[mesa],
            }
            datos_procesados.append(fila_convertida)
    except (ValueError, TypeError) as e:
        print(f"No se ha podido añadir los datos {e}")
    
    except FileNotFoundError:
        print("Fichero no encntrado")
        return None;
    except Exception as e:
        print(f"Error inesperado {e}")
        return None;

def insertar_reservar_bdd(conexion,reservas):
    sql_insertar = "INSERT INTO reserva (id,nombre,fecha,personas,mesa) VALUES (%s,%s,%s,%s,%s)"
    try:
        cursor = conexion.cursor()
        cursor.executemany(sql_insertar, reservas)
        print("Se han insertado las reservas")
    except pymysql.Error as e:
        print(f"No se ha podido introducir los datos {e}")

def mostrar_reservas_bbdd(ruta_csv,fecha):
    sql = "SELECT fecha FROM reservas"
    try:
        cursor = conexion.cursor()
        cursor.execute(sql,(fecha))
        return cursor.fetchall()
    except pymysql.Error as e:
        print(f"No se han podido cargar las fechas {e}")
        return []
    


    
    
    
    

    


    
    
