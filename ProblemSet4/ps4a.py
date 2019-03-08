# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):
    word=word.lower()
    total=0
    score=0
    for each in word:
        total+=SCRABBLE_LETTER_VALUES[each]
    if len(word) == n:
        score=total *(len(word)) +50
    else:
        score=total* (len(word))
    return score

def displayHand(hand):
    for letter in sorted(hand.keys()):
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def dealHand(n):
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    new_hand=hand.copy()
    for every in word:
        new_hand[every]=new_hand[every]-1
    return new_hand

def isValidWord(word, hand, wordList):
    def convertDictTolist(dic):
        st=[]
        for letter in dic.keys():
            for j in range(dic[letter]):
                st.append(letter)
        return st
    new_hand=convertDictTolist(hand)    
    if (word in wordList) :
        for each in word:
            if each in new_hand:
                new_hand.remove(each)
            else:
                return False
        return True
    else:
        return False


def calculateHandlen(hand):
    l=0
    for each in hand.values():
        l+=each
    return l


def playHand(hand, wordList, n):
    total=0
    while calculateHandlen(hand)!=0 :
        print ("Current Hand:",end="")
        displayHand(hand)
        entered=input('Enter word, or a "." to indicate that you are finished: ')
        if entered ==".":
            print ("Goodbye! Total score: "+str(total)+"points.")
            break
        else: 
            if isValidWord(entered,hand,wordList):
                total+=getWordScore(entered,n )
                print ('"',entered,'" earned',getWordScore(entered,n),'points. Total:',total,'points')
                print ()
                hand=updateHand(hand,entered)
            else:
                print ("Invalid word, please try again.")
                print ()
    else:
        print("Run out of letters. Total score:",total,"points.")
    

def playGame(wordList):
    value=0
    while True:
        char=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if char== 'n':
            n=HAND_SIZE
            hand=dealHand(n)
            playHand(hand,wordList,n)
            value=1
        elif char== 'r':
            if value==1:
                playHand(hand,wordList,n)
            else:
                print ("You have not played a hand yet. Please play a new hand first!")
        elif char== 'e':
            break
        else:
            print ("Invalid Command")

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
