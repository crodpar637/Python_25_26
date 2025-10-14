class Ejemplo:
    estatico = 7

    def __init__(self):
        self.instancia = 3


#instanciamos un par de objetos
a = Ejemplo()
b = Ejemplo()

print("a.instancia:", a.instancia)
print("b.instancia:", b.instancia)
a.instancia = 9
print("a.instancia:", a.instancia)
print("b.instancia:", b.instancia)

print("Ejemplo.estatico", Ejemplo.estatico)
print("a.estatico", a.estatico)
print("b.estatico:", b.estatico)

a.estatico = 10
print("Ejemplo.estatico", Ejemplo.estatico)
print("a.estatico", a.estatico)
print("b.estatico:", b.estatico)

a.estetico = 9








