class Game:

    def __init__(self,word,encryp_word,length_word):
        self.__word = word
        self.__encryp_word = encryp_word 
        self.__length_word = length_word

    def get_word(self):
        return " ".join(self.__word)
    def set_word(self,word):
        self.__word = word

    def get_encryp_word(self):
        return " ".join(self.__encryp_word)
    def set_encryp_word(self,encryp_word):
        self.__encryp_word = encryp_word

    def find_letter(self,letter):
        inserts = 0
        for idx in range(0,self.__length_word):
            if self.__word[idx] == letter:
                self.__encryp_word[idx] = letter
                inserts += 1
        if inserts > 0:
            result = True
        else:
            result = False

        return result
    

    def complete_word(self):
        result = False

        if self.__encryp_word == self.__word:
            result = True
        
        return result


    def look_life(self, life):
        result = False

        if life > 0:
            result = True

        return result