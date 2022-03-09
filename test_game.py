from game import Game
from player import Player

def test_data():
    palabra = "test".upper()
    palabra = [letra for letra in palabra]
    encriptado = ["_" for letra in palabra]
    cantidad_letras = len(palabra)
    return palabra,encriptado,cantidad_letras

palabra,encriptado,cantidad_letras = test_data()

new_game = Game(palabra,encriptado,cantidad_letras)


def run_game():
   
    print("Testeo de los metodos:")
    print("get_word")
    print("find_letter")
    print("get_encryp_word")
    print("complete_word")
    print("------------INIT--------------")
    print("get_word:",new_game.get_word())
    print("find_letter:",new_game.find_letter("E"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word",new_game.complete_word())
    print("--------------------------")
    print("get_word:",new_game.get_word())
    print("find_letter:",new_game.find_letter("T"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print("--------------------------")
    print("Palabra:",new_game.get_word())
    print("La palabra contiene la letra L?",new_game.find_letter("L"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print("--------------------------")
    print("get_word:",new_game.get_word())
    print("find_letter:",new_game.find_letter("S"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print()
    
    print("------------END--------------")
    print("Other test:")
    print("------------INIT--------------")
    
    life = 3
    response = new_game.look_life(life)
    while (response):   
        print("look_life:",response)
        print("life:",life)
        life -= 1   
        response = new_game.look_life(life)
        print()
    if life == 0:
        print("look_life:",response)
        print("life:",life)
    print("------------END--------------")
   
palabra = "test".upper()
palabra = [letra for letra in palabra]
encriptado = ["_" for letra in palabra]
cantidad_letras = len(palabra)
new_game = Game(palabra,encriptado,cantidad_letras)


def run_player():
   
    print("Testeo de los metodos:")
    print("get_word")
    print("find_letter")
    print("get_encryp_word")
    print("complete_word")
    print("------------INIT--------------")
    print("Palabra:",new_game.get_word())
    print("find_letter:",new_game.find_letter("E"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print("--------------------------")
    print("Palabra:",new_game.get_word())
    print("find_letter:",new_game.find_letter("T"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print("--------------------------")
    print("Palabra:",new_game.get_word())
    print("La palabra contiene la letra L?",new_game.find_letter("L"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print("--------------------------")
    print("Palabra:",new_game.get_word())
    print("find_letter:",new_game.find_letter("S"))
    print("get_encryp_word:",new_game.get_encryp_word())
    print("complete_word:",new_game.complete_word())
    print()
    
    print("------------END--------------")
    print("Testeo de los metodos:")
    print("look_life")
    print("------------INIT--------------")
    
    life = 3
    while (life > 0):
        response = new_game.look_life(life)
        if (response):
            print("Tiene "+str(life)+" vidas")
        life -= 1     
    if life == 0:
        print("perdiste")
    print("------------END--------------")

     

