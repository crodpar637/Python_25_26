x = float(input("Ingresa el valor para x: "))

# Cálculo de la fracción anidada
y =  1 / ( x + 1 / ( x + 1 / (x + 1 / x) ) )

print("y =", y) 

x = int(input())
y = int(input())

x = x // y
y = y // x

print( y ) 