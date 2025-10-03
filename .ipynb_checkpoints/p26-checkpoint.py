"""
Escriba un programa que utilizando listas pida al usuario los 9 números necesarios para
conformar una matriz de 3x3. Tras esto el programa mostrará la matriz introducida y también la matriz al cuadrado.
"""


def main():
    matriz = [ [] , [] , [] ]
    print(matriz)
    
    for i in range(0,3):
        for j in range(0,3):
            matriz[i].append(int(input("Dime un numero [" + str(i) + ","  + str(j) + "]:")))
    
    print(matriz)
    
    # Inicialización de matriz resultado
    matriz_resultado = [ [] , [] , [] ]
    
    # Recorrer filas matriz resultado
    for i in range(0,3):
        #Recorrer columnas matriz resultado
        for j in range(0,3):
            matriz_resultado[i].append(multiplicar_fila_columna(matriz, matriz, i , j) )

    print(matriz_resultado)

# Funcion que multiplica la fila f de la matriz m1 por la columna c de la matriz m2
def multiplicar_fila_columna(m1, m2, f , c): 

    valor = 0
    #Recorrer elementos de la fila f de la matriz m1, pero recorriendo por índice
    for i in range(0, len(m1[f])):
        valor = valor + m1[f][i] * m2[i][c]

    return valor
        
    
#Ejecución del programa principal
main()









    
    

