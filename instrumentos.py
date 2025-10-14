class Instrumento:
    def __init__ (self, precio):
        self.precio=precio
        
    def tocar(self):
        print ("Estamos tocando musica")
        
    def romper(self):
        print ("Eso lo pagas tu")
        print ("Son", self.precio, "$$$")


class Guitarra(Instrumento):
    def __init__ (self, precio, tipo_cuerda):
        # Instrumento.__init__(self, precio)    # lleva self
        super().__init__(precio)                # no lleva self
        self.tipo_cuerda=tipo_cuerda
    def tipo(self):
        print (self.tipo_cuerda)


g = Guitarra(100,'metal')

g.tipo()












    