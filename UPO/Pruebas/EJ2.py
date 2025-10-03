import sqlite3
import csv

# Función para exportar todos los clientes a un archivo CSV
def exportar_clientes_csv(nombre_bd, nombre_archivo):
    conn = sqlite3.connect(nombre_bd)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        csvfile = open(nombre_archivo, 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(['dni', 'nombre', 'direccion', 'telefono', 'correo', 'vip'])
        writer.writerows(clientes)
        print(f"Datos de clientes exportados correctamente al archivo '{nombre_archivo}'.")
    except sqlite3.Error as e:
        print("Error al exportar datos de clientes:", e)
    finally:
        csvfile.close()
        conn.close()

# Función para importar clientes desde un archivo CSV
def importar_clientes_csv(nombre_bd, nombre_archivo):
    conn = sqlite3.connect(nombre_bd)
    cursor = conn.cursor()
    try:
        csvfile = open(nombre_archivo, 'r', newline='')
        reader = csv.reader(csvfile)
        next(reader)  # Saltar la primera fila que contiene los encabezados
        for row in reader:
            cursor.execute("INSERT INTO clientes (dni, nombre, direccion, telefono, correo, vip) VALUES (?, ?, ?, ?, ?, ?)",
                           (row[0], row[1], row[2], row[3], row[4], int(row[5])))
        conn.commit()
        print(f"Datos de clientes importados correctamente desde el archivo '{nombre_archivo}'.")
    except sqlite3.Error as e:
        print("Error al importar datos de clientes:", e)
    finally:
        csvfile.close()
        conn.close()

# Función para exportar clientes VIP a un archivo CSV
def exportar_clientes_vip_csv(nombre_bd, nombre_archivo):
    conn = sqlite3.connect(nombre_bd)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes WHERE vip = 1")
        clientes_vip = cursor.fetchall()
        csvfile = open(nombre_archivo, 'w', newline='')
        writer = csv.writer(csvfile)
        writer.writerow(['dni', 'nombre', 'direccion', 'telefono', 'correo', 'vip'])
        writer.writerows(clientes_vip)
        print(f"Datos de clientes VIP exportados correctamente al archivo '{nombre_archivo}'.")
    except sqlite3.Error as e:
        print("Error al exportar datos de clientes VIP:", e)
    finally:
        csvfile.close()
        conn.close()

# Programa principal
def main():
    nombre_bd = 'clientes.db'
    while True:
        print("\nMenú:")
        print("(1) Exportar a fichero CSV")
        print("(2) Importar desde fichero CSV")
        print("(3) Exportar a fichero CSV los clientes VIP")
        print("(4) Terminar")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_archivo = input("Introduce el nombre del archivo CSV para exportar: ")
            exportar_clientes_csv(nombre_bd, nombre_archivo)
        elif opcion == "2":
            nombre_archivo = input("Introduce el nombre del archivo CSV para importar: ")
            importar_clientes_csv(nombre_bd, nombre_archivo)
        elif opcion == "3":
            nombre_archivo = input("Introduce el nombre del archivo CSV para exportar los clientes VIP: ")
            exportar_clientes_vip_csv(nombre_bd, nombre_archivo)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Introduce un número del 1 al 4.")

if __name__ == "__main__":
    main()
