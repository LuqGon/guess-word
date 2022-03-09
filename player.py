class Player:
    def __init__(self,name,lifes):
        self.__name = name
        self.__life = lifes

    def get_life(self):
        return self.__life
    def get_name(self):
        return self.__name

    def type_letter():
        letter = input("Ingrese una letra > ")
        return letter

    
    def life_lose(self):
        result = False
        if self.__life > 1: 
            self.__life -= 1
            result = True
        else:
            self.__life -= 1
            result = False
        
        assert self.__life >= 0, "Error! Vida negativa"
        return result


    
 


        