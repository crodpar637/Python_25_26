
es_par = lambda n : n % 2 == 0

print(es_par(8))

suma = lambda x,y : x + y

suma2 = suma

print(suma2(5,6))


l = [3,4,5,63,5,3,10]

resultado = filter( es_par, l)

for n in resultado:
    print(n)
    
print("mas datos")

for n in resultado:
    print(n)

