from game import Game
from player import Player
from menu_ import *
from menu_ import Menu
from os import system
import random_word
import test_game
system("clear")

def title():
    system("clear")
    '''Titulo del juego'''
    title = ""
    path = "guess_word/data/title.txt"
    with open(path,"r") as t:
        for line in t:
            title += line
    print(title)
    title = ""

def run():
    
    title()

    init_word,init_encryp_word,init_len_word = random_word.get()
    name = input("Ingrese su nombre >")
    system("clear")
    gamer = Player(name,50)
    guess_word = Game(init_word,init_encryp_word,init_len_word)
    menu = Menu()

    title()

    print("Bienvenido",name)
    init_option = menu.init_menu()
    if(init_option == 1):
        status_word = guess_word.get_word()
        status_encryp_word = guess_word.get_encryp_word()
        status_life = gamer.get_life() 
        flag = True
        while (flag):
            title()
            print("Lifes:",("♥️"*status_life))
            print(status_encryp_word)
            letter = input("Ingrese una letra >")#validar
            match_letter = guess_word.find_letter(letter.upper())
            
            if (not(match_letter)):
                gamer.life_lose()
                continue_game = guess_word.look_life(gamer.get_life())

                if (not(continue_game)):
                    flag = False
                    
            completed_game = guess_word.complete_word()

            if(completed_game):
                flag = False

            status_encryp_word = guess_word.get_encryp_word()
            status_life = gamer.get_life() 
            

        if (completed_game):
            print(status_encryp_word)
            print()
            print ("Ganaste")
            print()
        else:
            print(status_encryp_word)
            print()
            print ("Perdiste")
            print()
            print("La palabra era:",status_word)
            print()
    elif(init_option == 2):
        print(gamer.get_name())
    else:
        print("Adios")  
if __name__ == "__main__":
    run()
    