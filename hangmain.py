import string

def isWordGuessed(secretWord,letterGuessed):
    k=0
    for each in secretWord:
        if each in letterGuessed:
            k+=1
    if k==len(secretWord):
        return True
    else:
        return False
    
def getGuessedWord(secretWord, lettersGuessed):
    newWord=""
    for each in secretWord:
        if each in lettersGuessed:
            newWord+=each
        else:
            newWord+='_ '
    return newWord

def getAvailableLetters(lettersGuessed):
    fullLetters=string.ascii_lowercase
    available=''
    for each in fullLetters:
        if each not in lettersGuessed:
            available+=each
    return available

def hangmain(secretWord):
    print ("Welcomg to the game,Hangman!")
    print ("Iam thinking of a word that is",len(secretWord)," letters long.")
    letter=''
    chances=8
    letterGuessed=[]
    """
    Expected line: Oops! You've already guessed that letter: _ 
    Your code generated: Oops! That letter is not in my word:  _  ***
    """
    
    while chances>0 and not isWordGuessed(secretWord,letterGuessed):
        print ("-"*23)
        print ("You have ",chances," guesse left.")
        print ("Available Letters :", getAvailableLetters(letterGuessed)) 
        #print (getGuessedWord(secretWord, letterGuessed))
        letter=input("Please Guess a Letter: ")
        if letter in letterGuessed:
            print ("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, letterGuessed)),
        elif letter in secretWord:
            print ("Good Guess :",getGuessedWord(secretWord, letterGuessed)),
            letterGuessed.append(letter)
        else:
            chances-=1
            print ("Ooops! That letter is not in my word: ",getGuessedWord(secretWord, letterGuessed)),
            letterGuessed.append(letter)
        """
        if letter in secretWord:
            if letter in letterGuessed:
                print ("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, letterGuessed)),
                continue
            letterGuessed.append(letter)
            print ("Good Guess :",getGuessedWord(secretWord, letterGuessed)),
            pass
        else:
            chances-=1
            print ("Ooops! That letter is not in my word: ",getGuessedWord(secretWord, letterGuessed)),
            letterGuessed.append(letter)"""
    else:
        print ("-"*23)
        if (chances==0 and not isWordGuessed(secretWord,letterGuessed)):
            print ("Sorry, you ran out of guesses. The word was ",secretWord)
        elif (isWordGuessed(secretWord,letterGuessed)):        
            print ("Congratulations, you won!")



hangmain('c')
