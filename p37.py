#Introducción de datos de cuentas

cuenta = input("Introduzca una cuenta:")

cuentas = {}

while cuenta != 'x':
    importe = float(input("Importe:"))

    if cuenta in cuentas: # Comprobación de existencia de clave
        # Actualizar tupla de movimientos agregando el movimiento nuevo
        cuentas[cuenta] = cuentas[cuenta] + ( importe , ) # OJO constructor de tupla para un solo elemento
    else:
        # Nombre de cuenta nuevo --> elemento nuevo en el diccionario
        cuentas[cuenta] = ( importe , )
        
    cuenta = input("Introduzca una cuenta:")
    
print(cuentas)

lista_cuentas = []

for (k,v) in cuentas.items(): # En k se carga la clave y en v el valor
    lista_cuentas.append(  ( k , sum(v) ) )

print(lista_cuentas)  #  [ ('bar', 27 ) , ("futbol'), -10) ]

# elemento = ('bar', 27)  --> elemento[1]---> 27
lista_cuentas.sort(key= lambda elemento : elemento[1])  #ordenamos por el valor numerico de cada tupla

print("Cuenta con menor saldo:", lista_cuentas[0])
print("Cuenta con mayor saldo:", lista_cuentas[-1])












