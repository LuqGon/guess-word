def title():
    '''Titulo del juego'''
    title = ""
    path = "adivina_palabra/data/title.txt"
    with open(path,"r") as t:
        for line in t:
            title += line
    print(title)
    title = ""

def init_menu ():
    '''Menu del juego'''
    title()
    option = 0
    while(option < 1 or option > 3):
           print("1. Jugar!")
           print("2. Puntaje")
           print("3. Salir")
           option = int(input("Ingrese una opcion > "))
    return option

def difficulty_menu():
    option = 0
    print("Seleccione la dificultad")
    while(option < 1 or option > 3):
           print("1. Facil")
           print("2. Media")
           print("3. Dificil")
           option = int(input("Ingrese una opcion > "))
    return option