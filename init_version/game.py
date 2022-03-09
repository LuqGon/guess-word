def get_letter_life(word,word_encryp,letter_find):
    count_letters = len(word)
    count = 0
    for idx in range(0,count_letters):
        if word[idx] == letter_find:
            word_encryp[idx] = letter_find
            count += 1
    if count > 0:
        return word_encryp,False
    else:
        return word_encryp,True
            


            