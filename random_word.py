
from unidecode import unidecode
from random import choice

def get():
    '''Get random word'''
    path="guess_word/data/words.txt"
    with open(path, "r", encoding = "UTF-8") as words:
        list_word=[unidecode(word.upper()) for word in words ]
    words.close
    random_word = choice(list_word)
    send_random_word = [letter for letter in random_word if letter != '\n'] 
    '''Get encryp word '''
    send_encryp_word = ["_" for letra in send_random_word]
    '''Get length word '''
    send_lenght_word = len(send_random_word)
    return send_random_word, send_encryp_word, send_lenght_word

