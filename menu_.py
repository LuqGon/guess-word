class Menu:
    def __init__(self):
        self.__option_init = 0
        self.__option_diffi = 0

    def init_menu (self):
        '''Menu del juego'''
        while(self.__option_init < 1 or self.__option_init > 3):
           print("1. Jugar!")
           print("2. Puntaje")
           print("3. Salir")
           self.__option_init = int(input("Ingrese una opcion > "))
        return self.__option_init

    def difficulty_menu(self):
        print("Seleccione la dificultad")
        while(self.__option_diffi < 1 or self.__option_diffi > 3):
           print("1. Facil")
           print("2. Media")
           print("3. Dificil")
           self.__option_diffi = int(input("Ingrese una opcion > "))
        return self.__option_diffi
    


