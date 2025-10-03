# Crear las variables: juan, maria, y antonio.
# Asignar valores a las variables. El valor debe de ser igual al número de slimes que cada uno tiene. 
juan = 3
maria = 5
antonio = 7

# Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
print(juan, maria, antonio, sep=",")

# Después se debe crear una nueva variable llamada total_slimes y se debe igualar a la suma de las tres variables anteriores.
total_slimes = juan + maria + antonio

# Imprime el valor almacenado en total_slimes en la consola.
print("Total slimes:", total_slimes)
print(80 * "-")


# Suponiendo que cada uno de los slimes de Juan se fragmenta en 2 slimes medianos, los de María en 1 slime mediano y 
# en 2 slimes pequeños y los de Antonio la mitad (casi, un poco menos) de los que tenía se fragmentaron en 3 slimes 
# medianos y 4 slimes pequeños. 
# ¿Cuántos slimes y de qué tipo tienen en total? Realízalo usando variables, operaciones. La salida debería ser algo similar a:

# En total tienen: 
    ## slimes 
    ## slimes medianos 
    ## slimes pequeños


slimes_medianos = juan * 2 + maria * 1 + (antonio // 2) * 3
slimes = antonio - (antonio // 2)
slimes_pequeños = maria * 2 + (antonio // 2) * 4

print("En total tienen:")
print("\t",slimes, "slimes", sep=" ");
print("\t",slimes_medianos, "slimes_medianos", sep=" ")
print("\t",slimes_pequeños, "slimes_pequeños")
