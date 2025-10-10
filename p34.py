
d = {}

while len(d) < 5:
    trabajador = input("Dime un nombre:")
    dia = input("Dime el día:")

    if trabajador in d.keys(): # Comprobar si la clave existe en el diccionario
        print("El trabajador", trabajador, "ya tiene asignada una guardia")
    elif dia not in ['lunes','martes','miercoles','jueves','viernes']:
        print("El día", dia, "no es válido")
    elif dia in d.values():  # Comprobar si un valor existe en el diccionario
        print("El día", dia, "ya se ha asignado antes")
    else:
        d[trabajador] = dia

print(d)
            