#       Hangman game        #
#############################


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    check=0
    for each in secretWord:
        if each in lettersGuessed:
            check+=1
    if check==len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    newWord=""
    for each in secretWord:
        if each in lettersGuessed:
            newWord+=each
        else:
            newWord+=' _ '
    return newWord


def getAvailableLetters(lettersGuessed):
    fullLetters=string.ascii_lowercase
    available=''
    for each in fullLetters:
        if each not in lettersGuessed:
            available+=each
    return available

def hangman(secretWord):
    print ("Welcomg to the game,Hangman!")
    print ("Iam thinking of a word that is",len(secretWord)," letters long.")
    letter=''
    chances=8
    letterGuessed=[]
    while chances>0 and not isWordGuessed(secretWord,letterGuessed):
        print ("-"*23)
        print ("You have ",chances," guesse left.")
        print ("Available Letters :", getAvailableLetters(letterGuessed)) 
        #print (getGuessedWord(secretWord, letterGuessed))
        letter=input("Please Guess a Letter: ")
        if letter in letterGuessed:
            print ("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, letterGuessed)),
        elif letter in secretWord:
            letterGuessed.append(letter)
            print ("Good Guess :",getGuessedWord(secretWord, letterGuessed)),
        else:
            chances-=1
            print ("Oops! That letter is not in my word: ",getGuessedWord(secretWord, letterGuessed)),
            letterGuessed.append(letter)        
    else:
        print ("-"*23)
        if (chances==0 and not isWordGuessed(secretWord,letterGuessed)):
            print ("Sorry, you ran out of guesses. The word was ",secretWord)
        elif (isWordGuessed(secretWord,letterGuessed)):        
            print ("Congratulations, you won!")




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
