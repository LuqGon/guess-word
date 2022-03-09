from menu import *
from random_words import *
from game import * 
from os import system
system("clear")
if __name__ == '__main__':

    letter_word = ""
    option = init_menu()
    if option == 3:
        pass
    elif option == 2:
        pass
        #funcion
    else:
        system("clear")
        title()
        option = difficulty_menu()
        word,word_encryp= get_word(option)
        num_life = 3
        
        while True:
            system("clear")
            title()
            life = "♥️"*num_life

            if num_life == 0:
                system("clear")
                title()
                print("La palabra era: ", end="")
                for letter in word:
                    print(letter + " ", end="")
                print()
                print("Perdiste")
                break
            elif word_encryp == word:
                print("La palabra era: ", end="")
                for letter in word_encryp:
                    print(letter + " ", end="")
                print()
                print ("Ganaste")
                break
            else:

                print("Vidas: ",life)
                for letter in word_encryp:
                    print(letter + " ", end="")
                print()
                letter_player = input("Ingrese una letra > ").upper()

                word_encryp,response = get_letter_life(word,word_encryp,letter_player)
                
                if response:
                    num_life -= 1
            

            
           
       
    