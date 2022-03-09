from re import I
from unidecode import unidecode
from random import choice

def encryp_word_difficulty (type_dif,count_letter_word,list_letter_word):
    encryp_word = []
    
    for i in range(0, count_letter_word):
        if type_dif == 1:        
            if count_letter_word >= 7 and (i == 0 or i == count_letter_word-1 or i == count_letter_word // 2):
                encryp_word.append(list_letter_word[i])
            elif (count_letter_word >=5 and count_letter_word <7) and (i == 0 or i == count_letter_word-1):
                encryp_word.append(list_letter_word[i])
            elif count_letter_word < 5 and i == 0:
                encryp_word.append(list_letter_word[i])
            else:    
                encryp_word.append("_")
        if type_dif == 2:        

            if count_letter_word >= 7 and (i == 0 or i == count_letter_word-1):
                encryp_word.append(list_letter_word[i])
            elif (count_letter_word >=5 and count_letter_word <7) and i == 0:
                encryp_word.append(list_letter_word[i])
            else:    
                encryp_word.append("_")
        if type_dif == 3:        

            if count_letter_word >= 9 and (i == 0 or i == count_letter_word-1):
                encryp_word.append(list_letter_word[i])
            elif (count_letter_word >=7 and count_letter_word <9) and i == 0:
                encryp_word.append(list_letter_word[i])
            else:    
                encryp_word.append("_")
            
    return encryp_word   

def random_word(list_words,difficulty_type):
    
    random_word = choice(list_words)
    list_letter_word = [letter for letter in random_word if letter != '\n'] 
    count_letter_word=len(list_letter_word)
    list_encryp_word = encryp_word_difficulty(difficulty_type,count_letter_word,list_letter_word)

    return list_letter_word,list_encryp_word

def get_word(difficulty_type):

    '''Busca una palabra en el archivo words.txt y retorna un valor aleatorio'''

    path="adivina_palabra/data/words.txt"
    with open(path, "r", encoding = "UTF-8") as words:
        list_word=[unidecode(word.upper()) for word in words ]
    words.close
    word,encryp_word = random_word(list_word,difficulty_type)

    return word,encryp_word




