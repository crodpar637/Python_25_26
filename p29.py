def entrada_datos():
    numeros = []
    
    for i in range(0,5):
        num = int(input("Dime un numero:"))
        numeros.append(num)

    return tuple(numeros)

# Programa principal

numeros = entrada_datos()
l = [] 

for n in numeros:
    if n % 2 == 0: # Si es par
        l.append( ( n , 'PAR') )
    else:
         l.append( ( n , 'IMPAR') )

print("Números:", numeros)
print("Lista resultado: ", l)