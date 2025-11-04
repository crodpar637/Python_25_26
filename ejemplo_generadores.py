def mi_generador(n,m,s):
    while (n<=m):
        yield n
        n +=s

x = mi_generador(0, 5, 1)
print(x)

l = list(x)
print(l)

def otro_generador(l):
    while True:
        yield l[3]
        yield l[4]
        yield l[1]

y = otro_generador(l)


print(next(y))
print(next(y))  
print(next(y))
print(next(y))

def que_hace(l):
    n = -1
    while (n * -1) <= len(l):
        yield l[n]
        n -= 1

w = que_hace(l)

print(1,next(w))
print(2,next(w))
print(3,next(w))
print(4,next(w))
print(5,next(w))
print(6,next(w))
print(7,next(w))
print(8,next(w))





