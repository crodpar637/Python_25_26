def cargar_reservas_desde_csv():
    f = open("reservas.csv")
    ln = f.readLine()
    d = {}
    while ln != "":
        ln = f.readLine()
        ln.split(",")
        d[ln[0]] = (ln[1:5])
    f.close()
    return d

def insertar_reservas_bbdd(reservas):
    import mysql.connector
    db = mysql.connector.connect(host="localhost", user="root", password="test", database = "examen")
    mycursor = db.cursor()
    sql = ("INSERT INTO RESERVA VALUES (%s, %s, %s, %s, %s, %s)")
    valores = reservas.items();
    for valor in valores:
        mycursor.execute(sql, valor.items)