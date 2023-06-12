import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Desktop", "Recetas")


def contar_recetas(ruta): # Función para contar las recetas
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Mostrar menu inicio

def inicio():
    system("clear")
    print("*" * 50)
    print("*" * 5 + " Bienvenido al administrador de recetas " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentra en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción: ")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa""")
        eleccion_menu = input()
    return int(eleccion_menu)


def mostrar_categorias(ruta): # Función para mostrar las categorias
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return  lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta): # Función para mostrar las recetas
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)

    return lista_recetas

def elegir_recetas(lista): #Función elegir las recetas
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta): # Función para crear una receta nueva
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")


def crear_categoria(ruta): # Función para crear una categoria nueva
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoría {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe")



def eliminar_receta(receta): #Función para eliminar receta
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoría {categoria.name} ha sido eliminada")


def volver_inicio(): # Función para volver al inicio
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresione V para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:


    menu = inicio()

    if menu == 1:
        # Función mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Función elegir categorías
        mi_categoria = elegir_categoria(mis_categorias)
        # Función mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # Función elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        # Función leer receta
        leer_receta(mi_receta)
        # Función volver inicio
        volver_inicio()

    elif menu == 2:
        # Función mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Función elegir categorías
        mi_categoria = elegir_categoria(mis_categorias)
        # Función crear receta nueva
        crear_receta(mi_categoria)
        # Función volver inicio
        volver_inicio()

    elif menu == 3:
        # Función crear categoría nueva
        crear_categoria(mi_ruta)
        # Función volver inicio
        volver_inicio()

    elif menu == 4:
        # Función mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Función elegir categorías
        mi_categoria = elegir_categoria(mis_categorias)
        # Función mostrar recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # Función elegir recetas
        mi_receta = elegir_recetas(mis_recetas)
        # Función eliminar receta
        eliminar_receta(mi_receta)
        # Función volver inicio
        volver_inicio()

    elif menu == 5:
        # Función mostrar categorias
        mis_categorias = mostrar_categorias(mi_ruta)
        # Función elegir categorías
        mi_categoria = elegir_categoria(mis_categorias)
        # Función eliminar categorias
        eliminar_categoria(mi_categoria)
        # Función volver inicio
        volver_inicio()

    elif menu == 6:
        # Función eliminar programa
        finalizar_programa = True
