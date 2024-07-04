
import os
class pelicula:
    def __init__(self, nombre, genero, duracion, año, __raiting):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.año = año
        self.__raiting = __raiting

class Catalogo (pelicula):
    def __init__(self, nombre, genero, duracion, año, __raiting, ruta_archivo):
        super().__init__(nombre, genero, duracion, año, __raiting)
        self.ruta_archivo = ruta_archivo

    def get_movies(self):

        f = open(self.ruta_archivo, "r")   # Changed 'l' to 'r' for reading the file
        print(f.read())
        f.close()

    @classmethod
    def add_movie(self, pelicula):
        f= open(self.ruta_archivo, "a")   
    
        # Removed the erroneous lines and adjusted indentation
        f.write(pelicula + "," + "\n")    
        f.close()
        return("La pelicula se ha añadido")
            
    def remove_movie(self): 
        try: 
            f= open(self.ruta_archivo, "r")
        except FileNotFoundError:
            return "!El catalogo no existe\n"
    

lista_peliculas = ['Romeo y Julieta', 'Romero', 'Pyton']
filename = "catalogo.txt"
file_directory = "movie"

# Create the directory if it doesn't exist
if not os.path.exists(file_directory):
    os.makedirs(file_directory)

file = os.path.join(file_directory, filename) # Construct the full file path

with open(file, 'a+') as f:
    for i in lista_peliculas:
        f.write(i)

mi_path = "catalogo.txt"

with open(mi_path, 'a+') as f:
    for i in lista_peliculas:
        f.write(i)

file_directory = "movies"

if not os.path.exists(file_directory):
    os.makedirs(file_directory)
    pelicula_1 = pelicula("Pyton", "terror", 1.50, 2000, 3.00)
    pelicula_2 = pelicula("Sonrie", "terror", 1.56, 2022, 3.6)
    pelicula_3 = pelicula("Siniestro", "terror", 1.50, 2012, 4.2)
    movies = [pelicula_1, pelicula_2, pelicula_3]
    print("movies")

def menu():
    
    menu = "Escriba la opcion deseada"
    print(menu)

    
    print('Gestión del directorio de peliculas')
    print('============================')
    print('1 - Listar las peliculas')
    print('2 - Añadir una pelicula')
    print('3 - Eliminar un pelicula')
    print('4 - Crear el directorio')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option


def file_directory():
   
    d = file_directory("catalogo", "catalogo.txt")

    while True:
        option = menu()
        if option == '1':
            print(d.get_movies())
        elif option == '2':
            nombre_pelicula = input('Introduce el nombre de la pelicula: ')
            genero = input('Introduce el teléfono del cliente: ')
            pelicula = pelicula(nombre_pelicula)
            print(d.add_movie(pelicula_1))
        elif option == '3':
            pelicula = input('Introduce el nombre de la pelicula: ')
            print(d.remove_movie(nombre_pelicula))
        elif option == '4':
            print(d.create_directory())
        elif option == '0':
            break
        else:
          print("Ingrese una opción válida")
    return

    print("Su catalogo ha sido actualizado")
    file_directory



    