def entrada_datos():
    palabra = ""
    l = []
    
    palabra = input("Dime una palabra ('fin' para terminar):")
    while palabra != 'fin':
        l.append(palabra)
        palabra = input("Dime una palabra ('fin' para terminar):")

    return l

# Programa principal
l = entrada_datos()
vocales = []
consonantes = tuple() # tupla vacía

for palabra in l:
    if palabra[0] in ['a','e','i','o','u','A','E','I','O','U']:
        if not palabra in vocales:
            vocales.append(palabra)
    else:
        if not palabra in consonantes:
            consonantes = consonantes + (palabra,) #concatenación de tuplas -> se crea una nueva

print("Lista de palabras:", l)
print("Palabras que comienzan por vocal:", vocales)
print("Palabras que comienzan por consonante:", consonantes)
    