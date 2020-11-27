
# version 1.0

import random
import os

try:
    #find current dir 
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    #attach wordlist file name to path
    # if you want your wordlist just name the file below
    my_file = os.path.join(THIS_FOLDER, 'wordlist.txt')
    #open wordlist file
    file = open(my_file)
    lines = file.readlines()
    #choose a random word 
    random_word = random.choice(lines).strip()
    # vars
    wrong_guess = 0
    well_guess = 0
    found_alpha = []
    word_progress = []
    # show space for length of word
    for item in random_word:
        word_progress.append('-')
    if well_guess == 0:
        print('guess this word :: ')
        print('-'*len(random_word))
    # gamer has 5 choose and if he/she lost them... the game will be over
    while wrong_guess < 5:
        #get guess char
        guess = input('Please guess alphabets ::  ').strip()
        # try to force gamer to choose one char
        if len(guess) == 1:
            if guess in random_word:
                if guess in found_alpha:
                    print('wow you found it before !!!')
                    print('#############################')
                else:
                    print('congratulation !!! guess next')
                    print('#############################')
                    well_guess += 1
            else:
                wrong_guess += 1
                print('No it is not have " %s " ---> %s / 5' % (guess,wrong_guess))
                print('#############################')
                
        else:
            print('No No just guess alphabets one by one!!!')
            print('#############################')
        start1 = 0
        end1 = len(random_word)
        # try to find chars that was duplicated
        for item in random_word:
            if item == guess:
                for i in range(random_word.count(item)):
                    word_progress[random_word.find(item,start1)]=item
                    start1 = random_word.find(item,start1)+1
                found_alpha.append(item)
                break
        print(''.join(word_progress))
        
        if '-' not in ''.join(word_progress) :
            print('#############################')
            print('wonderful the word is \n\"%s\"\nYOU did it \nDONE!!!'%random_word)
            print('#############################') 
            file.close()
            break

    if wrong_guess == 5 :
        print('#############################')
        print('word is :   %s'%random_word)
        print('Game Over ... Please try again')
        print('#############################')
        file.close()

except:
    print('Some Problems has been occurred !!!')
    file.close()
