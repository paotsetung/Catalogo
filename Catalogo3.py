import os

class pelicula:
    def __init__(self, nombre, genero, duracion, año, __raiting):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.año = año
        self.__raiting = __raiting

class Catalogo(pelicula):
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo

        with open(self.ruta_archivo, 'x') as ra:
            pass

    def get_movies(self):
        f = open(self.ruta_archivo, "r")
        print(f.read())
        f.close()

   
    def add_movie(self, pelicula):  
        with open(self.ruta_archivo, "a") as f:
            f.write(pelicula.nombre + "," + "\n")
        return("La pelicula se ha añadido")
    
d = Catalogo(nombre_catalogo,nombre_catalogo+'.txt')
    def remove_movie(self, d):
        try:
            f = open(self.ruta_archivo, "r")
        except FileNotFoundError:
            return "!El catalogo no existe\n"


def menu():
    
    menu = "Escriba la opcion deseada"
    print(menu)

    
    print('Gestión del directorio de peliculas')
    print('============================')
    print('1 - Listar las peliculas')
    print('2 - Añadir una pelicula')
    print('3 - Eliminar el catálogo')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def file_directory():
   
    nombre_catalogo = input("Ingrese el nombre del catalogo: ")
    d = Catalogo(nombre_catalogo,nombre_catalogo+'.txt')

    while True:
        option = menu()
        if option == '1':
            print(d.get_movies())
        elif option == '2':
            nombre_pelicula = input('Introduce el nombre de la pelicula: ')
            genero = input('Introduce el genero: ')  
            duracion = input('Introduce la duracion: ')
            año = input('Introduce el año: ')
            raiting = input('Introduce el __raiting: ')
            peli = pelicula(nombre_pelicula, genero, duracion, año, raiting) 
            print(d.add_movie(peli))
        elif option == '3':
            nombre_pelicula = input('Introduce el nombre del catálogo: ')
            print(d.remove_movie(d))
        elif option == '0':
            break
        else:
          print("Ingrese una opción válida")
    return

    print("Su catalogo ha sido actualizado")
    
file_directory()