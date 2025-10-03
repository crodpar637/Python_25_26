"""
Escriba un programa que pida la introducción de seis números al usuario, los tres primeros se
almacenarán en una lista y se ordenarán, los siguientes se almacenarán en otra lista y también
se ordenarán. Se mostrará por pantalla el contenido de la primera lista, el contenido de la
segunda lista y una tupla conformada por los seis elementos en el orden que se obtenga de
concatenar la primera y la segunda lista
"""

l1 = []
l2 = []

for i in range(0,3):
    l1.append(int(input("Introduzca un numero para la primera lista:")))
    l2.append(int(input("Introduzca un numero para la segunda lista:")))
    
l3 = l1[:] # hacemos una copia [:] 
l4 = l2[:]
l3.sort()
l4.sort()

print(l1, l3)
print(l2, l4)

t = tuple(l3) + tuple(l4)
print(t)







