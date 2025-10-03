l = [99, True, "una lista", [1, 2]]

l[0:2] = [1,2,3]

print(l)

cuentas = [(300,450),(400,300),(500,350),(450,300)]
impares = cuentas[::2]
print("Impares",impares)
pares = cuentas[1::2] 
print("Pares",pares)
dos_primeros = cuentas[:2] 
print("Dos Primeros",dos_primeros)
dos_ultimos = cuentas[-2:]
print("Dos Ultimos",dos_ultimos)
primero_y_ultimo = cuentas[0::len(cuentas)-1]
print("Primero y ultimo:", primero_y_ultimo)

primero_y_ultimo = [ cuentas[0] , cuentas[-1] ]
print("Primero y ultimo:", primero_y_ultimo)

primero_y_ultimo = [ cuentas[0] ] + [ cuentas[-1] ]
print("Primero y ultimo:", primero_y_ultimo)





