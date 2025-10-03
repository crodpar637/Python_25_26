import sqlite3


# Función para crear la tabla de clientes si no existe
def crear_tabla_clientes():
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        nif TEXT PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        direccion TEXT,
                        telefono TEXT,
                        correo TEXT,
                        vip INTEGER
                        )''')
        print("Tabla de clientes creada correctamente.")
    except sqlite3.Error as e:
        print("Error al crear la tabla de clientes:", e)


# Función para añadir un cliente a la base de datos
def añadir_cliente():
    nif = input("Introduce el NIF del cliente: ")
    nombre = input("Introduce el nombre del cliente: ")
    direccion = input("Introduce la dirección del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    correo = input("Introduce el correo del cliente: ")
    vip = int(input("¿Es cliente VIP? (0: No, 1: Sí): "))

    try:
        conn.execute("INSERT INTO clientes (nif, nombre, direccion, telefono, correo, vip) VALUES (?, ?, ?, ?, ?, ?)",
                     (nif, nombre, direccion, telefono, correo, vip))
        conn.commit()
        print("Cliente añadido correctamente.")
    except sqlite3.Error as e:
        print("Error al añadir cliente:", e)


# Función para eliminar un cliente de la base de datos
def eliminar_cliente():
    nif = input("Introduce el NIF del cliente que deseas eliminar: ")
    try:
        conn.execute("DELETE FROM clientes WHERE nif = ?", (nif,))
        conn.commit()
        print("Cliente eliminado correctamente.")
    except sqlite3.Error as e:
        print("Error al eliminar cliente:", e)


# Función para mostrar los datos de un cliente a partir de su NIF
def mostrar_cliente():
    nif = input("Introduce el NIF del cliente que deseas mostrar: ")
    try:
        cursor = conn.execute("SELECT * FROM clientes WHERE nif = ?", (nif,))
        cliente = cursor.fetchone()
        if cliente:
            print("Datos del cliente:")
            print("NIF:", cliente[0])
            print("Nombre:", cliente[1])
            print("Dirección:", cliente[2])
            print("Teléfono:", cliente[3])
            print("Correo:", cliente[4])
            print("VIP:", "Sí" if cliente[5] else "No")
        else:
            print("Cliente no encontrado.")
    except sqlite3.Error as e:
        print("Error al mostrar cliente:", e)


# Función para listar todos los clientes
def listar_clientes():
    try:
        cursor = conn.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        if clientes:
            print("Lista de clientes:")
            for cliente in clientes:
                print("NIF:", cliente[0])
                print("Nombre:", cliente[1])
                print("Dirección:", cliente[2])
                print("Teléfono:", cliente[3])
                print("Correo:", cliente[4])
                print("VIP:", "Sí" if cliente[5] else "No")
                print()
        else:
            print("No hay clientes registrados.")
    except sqlite3.Error as e:
        print("Error al listar clientes:", e)


# Función para listar clientes VIP
def listar_clientes_vip():
    try:
        cursor = conn.execute("SELECT * FROM clientes WHERE vip = 1")
        clientes_vip = cursor.fetchall()
        if clientes_vip:
            print("Lista de clientes VIP:")
            for cliente in clientes_vip:
                print("NIF:", cliente[0])
                print("Nombre:", cliente[1])
                print("Dirección:", cliente[2])
                print("Teléfono:", cliente[3])
                print("Correo:", cliente[4])
                print()
        else:
            print("No hay clientes VIP registrados.")
    except sqlite3.Error as e:
        print("Error al listar clientes VIP:", e)


# Conexión a la base de datos
conn = sqlite3.connect('clientes2.db')
crear_tabla_clientes()

# Menú principal
while True:
    print("\nMenú:")
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente a partir de su NIF")
    print("(4) Listar todos los clientes")
    print("(5) Listar clientes VIP")
    print("(6) Terminar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_cliente()
    elif opcion == "2":
        eliminar_cliente()
    elif opcion == "3":
        mostrar_cliente()
    elif opcion == "4":
        listar_clientes()
    elif opcion == "5":
        listar_clientes_vip()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Introduce un número del 1 al 6.")

# Cerrar conexión
conn.close()
