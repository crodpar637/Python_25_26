import pymysql

def cargar_reservas_desde_csv():
    f = open('reservas.csv', 'r', encoding = 'utf-8')
    lineas = f.readlines()
    dict_datos = {}
        
    for linea in lineas[1:]:
        campo = linea.strip().split(',')
        dict_values = {}
        dict_values['nombre'] = campo[1]
        dict_values['telefono'] = campo[2]
        dict_values['fecha'] = campo[3]
        dict_values['personas'] = campo[4]
        dict_values['mesa'] = campo[5]

        dict_datos[campo[0]] = dict_values

    print(dict_datos)
    return dict_datos

"""def intentar_reservas_bbdd(reservas):
    connection = pymysql.connect(
        host="db",      # IP del host Docker
        user="root",
        password="test",
        database="examen",
        port=3306
    )
    cursor = connection.cursor()
    for fila in reservas.keys():
        id = fila
        nombre = ''
        telefono = ''
        fecha = ''
        personas = ''
        mesa = ''
        for valor in fila:
            nombre = valor[0]
            telefono = valor[1]
            fecha = valor[2]
            personas = valor[3]
            mesa = valor[4]

        cursor.execute('INSERT INTO reserva (`id`, `nombre_cliente`, `telefono`, `fecha_reserva`, `numero_personas`, `numero_mesa`) VALUES ('+ id + ',' + nombre + ',' + telefono + ',' + fecha + ',' + personas + ',' + mesa + ');')

"""

def main():
    cargar_reservas_desde_csv()
    #intentar_reservas_bbdd(diccionario)


if __name__ == '__main__':
    main()