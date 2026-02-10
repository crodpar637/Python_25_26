from functools import reduce

class MovieCollection():
    def __init__(self):
        self.__movies = []

    def add_movie(self, title, director, duration, genre="Desconocido"):
        encontrado = False
        
        for peli in self.__movies:
            if peli[0] == title:
                encontrado = True
                break # me salgo porque he encontrado la peli

        if encontrado:
            return "La pelicula ya existe previamente: " + title
        else:
            #Agrego la pelicula como tupla
            tupla = (title, director, duration, genre)
            self.__movies.append( tupla )
            
            return "La pelicula se ha registrado"

    def add_advertisement(self,minutes):

        l = [] #lista nueva
        
        for peli in self.__movies:
            tupla_nueva = ( peli[0],peli[1],peli[2]+minutes, peli[3] ) #creación de tupla
            l.append ( tupla_nueva )

        self.__movies = l # sustituyo la lista de pelis por la nueva


    def movies_by_genre(self,genre):

        obj_filtro = filter(lambda peli : peli[3] == genre, self.__movies)

        obj_map = map(lambda peli : peli[0], obj_filtro)

        return list(obj_map)

    def movies_by_genre_bucle(self,genre):
        l = []

        for peli in self.__movies:
            if peli[3] == genre:
                l.append(peli[0]) # solo los títulos

        return l

    def __str__(self):
        s = ""
        for peli in self.__movies:
            s += peli[0] + " - " + peli[1] + " - " + str(peli[2]) + "\n"

        return s

    def toString(self): 

        obj_map = map(lambda peli :  peli[0] + " - " + peli[1] + " - " + str(peli[2]) + "\n", self.__movies)
        
        s = reduce(lambda cadena, peli: cadena + peli, obj_map, "")
        
        return s

#  PROGRAMA PRINCIPAL
def main():
    # Instanciar objeto
    coleccion_pelis = MovieCollection()

    print(coleccion_pelis.add_movie("El arca perdida", "Steven Spielberg", 120, "Aventuras"))
    print(coleccion_pelis.add_movie("El arca perdida", "Steven Spielberg", 120, "Aventuras"))
    print(coleccion_pelis.add_movie("El templo maldito", "Steven Spielberg", 150, "Aventuras"))
    print(coleccion_pelis.add_movie("La ultima cruzada", "Steven Spielberg", 130, "Comedia"))
    print(coleccion_pelis.add_movie("La calavera de cristal", "Steven Spielberg", 140, "Aventuras"))
    print(coleccion_pelis.add_movie("El dia del destino", "Steven Spielberg", 160, "Drama"))

    print(coleccion_pelis)

    coleccion_pelis.add_advertisement(5)

    print(coleccion_pelis.toString() )

    l = coleccion_pelis.movies_by_genre_bucle("Aventuras")
    print(l)

    l = coleccion_pelis.movies_by_genre("Drama")
    print(l)
    

if __name__ == "__main__":
    main()
    
        

    

        



