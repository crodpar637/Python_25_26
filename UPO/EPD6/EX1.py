from math import sqrt

def solve(a, b, c):
    # Comprobamos si la solución no existe
    discriminante = b*b - 4*a*c
    if discriminante > 0:
      sol1 = (- b + sqrt(discriminante)) / (2*a)
      sol2 = (- b - sqrt(discriminante)) / (2*a)
      print("Solucion 1: ", sol1)
      print("Solucion 2: ", sol2)
    elif discriminante == 0:
      sol = (- b) / (2*a)
      print("Solución: ", sol)
    else:
      print("No tiene solución")

input("dime un numero")
solve(1, 6, 8)
solve(1, -4, 4)
solve(2, 2, 2)