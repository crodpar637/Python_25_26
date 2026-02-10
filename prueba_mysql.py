import pymysql

connection = pymysql.connect(
    host="db",      # nombre del server en docker
    user="root",
    password="test",
    database="libreria",
    port=3306
)

cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print("Versión de MySQL:", version)

connection.close()