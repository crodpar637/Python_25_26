import sqlite3
import os

def cargar_inventario():
    inventario = {}
    with open('./EJ2/libros.csv', 'r', encoding="UTF-8") as file:
        next(file)  # Saltar la cabecera
        for line in file:
            titulo, precio, copias = line.strip().split(',')
            inventario[titulo] = (float(precio), int(copias))
    return inventario

def actualizar_copias_vendidas(inventario, libro, copias_vendidas):
    if libro in inventario:
        precio, copias = inventario[libro]
      
        if copias >= copias_vendidas:
            inventario[libro] = (precio, copias - copias_vendidas)
            return True
    else:
        print(libro, " no en inventario")
    return False

def libros_pocas_copias(inventario, limite):
    return list(filter(lambda x: inventario[x][1] < limite, inventario))

def guardar_en_bd(inventario):
    os.remove('./EJ2/libreria.db')
    conn = sqlite3.connect('./EJ2/libreria.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS libros
                      (nombre TEXT, precio REAL, copias INTEGER)''')
    for libro, (precio, copias) in inventario.items():
        cursor.execute("INSERT INTO libros VALUES (?, ?, ?)", (libro, precio, copias))
    conn.commit()
    conn.close()

def main():
    inventario = cargar_inventario()
    print("Inventario cargado:", inventario)

    libro = "Crimen y castigo"
    copias_vendidas = 5
    resultado = actualizar_copias_vendidas(inventario, libro, copias_vendidas)
    print(f"Actualización de copias vendidas para '{libro}': {resultado}")

    limite = 5
    libros_bajo_limite = libros_pocas_copias(inventario, limite)
    print("Libros con pocas copias:", libros_bajo_limite)

    guardar_en_bd(inventario)
    print("Datos guardados en la base de datos.")

if __name__ == "__main__":
    main()