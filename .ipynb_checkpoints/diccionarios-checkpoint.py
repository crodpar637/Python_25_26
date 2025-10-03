# Crear un diccionario vacio
d = {}

# Crear un diccionario con datos
d1 = { 5 : "Bingo", "Sevilla" : True, False : ( 2, 4) }

# Agregar elementos 
d["k1"] = "v1"
d["k2"] = "v2"
d1["k3"] = "v3"
d1["k1"] = "v1 - nuevo"
# Modificar el varlor de una clave existente
d1[5] = "Linea"

print(" d: ", d)
print(" d1: ", d1)

#Agregan claves nuevas y se machacan valores de claves exitentes
d.update(d1)

print(" d: ", d)
print(" d1: ", d1)

# Recorridos de diccionarios
print("Recorrido de diccionarios")
print("Recorrido por claves")
for k in d:   # Equivalente for k in d.keys():
    print("Clave:", k)

print("Recorrido por valores")
for v in d.values():
    print("Valor:", v)

print("Recorrido por elementos")
for e in d.items():
    print("Elemento:", e, "Clave:" , e[0] , "Valor:", e[1])

print("Recorrido por elementos v2")
for (k,v) in d.items():
    print("Clave:" , k , "Valor:", v)

print(d.keys())
print(d.values())
print(d.items())


print(d.get(6,"No existe"))








