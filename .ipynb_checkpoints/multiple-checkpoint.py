class A:
    def __init__(self):
        print("Inicializando A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Inicializando B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Inicializando C")

class F(A):
    def __init__(self):
        super().__init__()
        print("Inicializando F")
        
class D(F , B, C):
    def __init__(self):
        super().__init__()
        print("Inicializando D")

d = D()
print(D.__mro__)
print("Hola")
