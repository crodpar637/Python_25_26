def ordenar(equipo):
    return equipo[1]
    
def entrada_datos():
    datos = []

    # introducción de datos de 3 equipos y sus resultados en la liga
    for i in range(0,3): 
        equipo = input("Dime el equipo:")
        ganados = int(input("¿Cuántos partidos ha ganado?"))
        perdidos = int(input("¿Cuántos partidos ha perdido?"))
        empatados = int(input("¿Cuántos partidos ha empatado?"))
        
        datos.append( (equipo, ganados, perdidos, empatados ) )

    return datos

# Programa principal
datos = entrada_datos()
resultado = []

for equipo in datos:
    puntos = equipo[1] * 3 + equipo[2] * 0 + equipo[3] * 1
    resultado.append( ( equipo[0], puntos) ) 

# El parametro key recibe una función, que dado un elemento de la lista, 
# devuelve el valor a tener en cuenta para ordenar
resultado.sort(key=lambda equipo: equipo[1])
resultado.sort(key=ordenar)
resultado.reverse()

print("Equipos y datos de partidos:", datos)
print("Equipos, puntos y clasificación (datos ordenados):", resultado)

    







