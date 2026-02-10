#import MySQLdb
import pymysql

def getConnection():
    db_host = 'db'
    usuario = 'root'
    clave = 'test'
    base_de_datos = 'empresa'
    #conn = MySQLdb.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)
    conn = pymysql.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)
    
    return conn

# Obtengo la conexión
conn = getConnection()

# Obtener cursor
cursor = conn.cursor()

# Ejecutar sentencias
cursor.execute("SELECT * FROM componente")

# Obtengo todas las filas que devuelve la consulta
rows = cursor.fetchall()
# Cerrar conexion
conn.close()

for r in rows:
    print(r)


# Obtengo la conexión
conn = getConnection()

# Obtener cursor
cursor = conn.cursor()

# Ejecutar sentencias
cursor.execute("SELECT * FROM componente")

# Recorro el resultado usando el cursor como un iterador
for fila in cursor:
    print("idcomponente",fila[0])
    print(fila)

cursor.execute("SELECT * FROM tipo")
# Recorro el resultado usando fetchone
fila = cursor.fetchone()
while fila:
    print("idtipo",fila[0])
    print(fila)
    fila = cursor.fetchone()
    
# Cerrar conexion
conn.close()



