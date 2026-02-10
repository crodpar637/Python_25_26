import pymysql

#a
def cargar_reservas_desde_csv():
    f= open("reservas.csv","r", encoding="utf-8")
    lineas=f.readlines()
    f.close
    campos=list()
    for linea in lineas[1:]:
        campos.append(linea.strip().split(","))
    return campos

#b
def insertar_reservas_bbdd(reservas):
    connection=getConexion()
    
    cursor=connection.cursor()
    for reserva in reservas:
        sql = "INSERT INTO reserva VALUES (%s,%s,%s,%s,%s,%s);"
        val = (reserva[0], reserva[1], reserva[2],reserva[3],reserva[4],reserva[5])
        cursor.execute(sql, val)
        
    connection.commit()
    connection.close()
    

#c
def mostrar_reservas_fecha(fecha):
    connection=getConexion()

    cursor=connection.cursor()

    sql = "SELECT * FROM reserva WHERE fecha_reserva=%s;"
    val = (fecha)
    cursor.execute(sql, val)
    
    resultado = cursor.fetchall()
    connection.close()
    print("RESERVAS PARA "+fecha+": ")
    print("========================")
    for r in resultado:
        print("Mesa "+str(r[5])+": "+r[1]+" ("+str(r[4])+") - Tel: "+str(r[2]))
    


def main():
    reservas=cargar_reservas_desde_csv()
    print(reservas)
    
    insertar_reservas_bbdd(reservas)
    
    mostrar_reservas_fecha("2025-03-15")
    

def getConexion():
    connection = pymysql.connect(
        host="db",      # IP del host Docker
        user="root",
        password="test",
        database="examen",
        port=3306
    )
    return connection


if __name__=="__main__":
    main()