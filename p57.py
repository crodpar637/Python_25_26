from functools import reduce


diccionario = { ("ferry",1) : [ 2500 ,350 ], # [ carga, pasajeros ]
                ("mercante",2) : [ 120000, 6500 ], # [ carga, autonomía ]
                ("mercante",3) : [ 200000, 3200 ], # [ carga, pasajeros ]
                ("ferry",4) : [ 3520 , 420] , # [ carga, pasajeros ]
              }

"""
Escriba una función obtenerPasajeros(diccionario), que tomando como parámetro de
entrada el diccionario anterior, devuelva una tupla con los pasajeros de cada ferry.
"""
def obtener_pasajeros1(d):
    l = [] 
    for k,v in d.items():
        if k[0] == "ferry": #verifico si es un ferry
            l.append( v[1] )     #obtengo pasajeros

    return tuple(l)

def obtener_pasajeros2(d):
   #proceso de filtrado
    # d.items --> [ ( k1, v1) , (k2,v2), ...] --> [ ( ("ferry",1), [ 2500 ,350 ]) , ( ("mercante",2) , [ 120000, 6500 ], ...  ]
    ferrys = filter(lambda item : item[0][0] == "ferry"  , d.items() ) 

    pasajeros = map(lambda item : item[1][1], ferrys)

    return tuple(pasajeros)

print(obtener_pasajeros1(diccionario))
print(obtener_pasajeros2(diccionario))


l = [1,2,3,6,7,]

l2 = map(lambda n : n+1, l)

print(list(l2))

def mayor_carga(d):
    mercantes = filter(lambda item : item[0][0] == "mercante"  , d.items() )

    mercante_mayor_carga = reduce(lambda it1, it2 : it1 if it1[1][0] > it2[1][0] else it2, mercantes)

    return [ mercante_mayor_carga[0][1] ]

print(mayor_carga(diccionario))
    






