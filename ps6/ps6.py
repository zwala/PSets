import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        lower=string.ascii_lowercase
        upper=string.ascii_uppercase
        all_letters=string.ascii_letters
        d={}
        for let in all_letters:
            if let in lower:
                ind=all_letters.index(let)
                new=ind+shift
                if new>25:
                    new=new-26
                d[let]=all_letters[new]
            elif let in upper:
                ind=all_letters.index(let)
                new=ind+shift
                if new>51:
                    new=new-26
                d[let]=all_letters[new]
        return d
              

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        d=self.build_shift_dict(shift)
        message=self.message_text
        cipher_text=""
        for each in message:
            if each in string.punctuation:
                cipher_text+=each
            elif each==" ":
                cipher_text+=each
            elif each in string.digits:
                cipher_text+=each
            else:
                cipher_text+=d[each]
        return cipher_text
                

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text=text
        self.valid_words=load_words('words.txt')
        self.shift=shift
        self.encrypting_dict=self.build_shift_dict(self.shift)
        self.message_text_encrypted=self.apply_shift(self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        newDic=self.build_shift_dict(self.shift)
        return newDic

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if (shift!=self.shift):
            self.shift=shift
            self.encrypting_dict=self.build_shift_dict(shift)
            self.message_text_encrypted=self.apply_shift(shift)

#function: load_wordS(file_name) returns:word_list
#function: is_word(word_list ,word)
#function: get_story_string() :returns story in string format
#class: Message: (takes in text message)
            #get_message_text
            #get_valid_words from word.txt file
            #build_dict
            #apply_shift
#class:PlainTextMessage (child class of 'Message' class)
            #get_shift
            #get_encrypting_dict
            #get_message_text_encrypted
            #change_shift
#Class: CiphertextMessage :child class of 'Message'            
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #cipher_Text= 'Mjqqt'
        #decrypt_message -->> (5,'Hello' )
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        original=self.message_text
        dc_list=self.message_text.split(" ")
        d={}
        for each in range(1,26):
            shift=26-each
            d[shift]=0
            for each in dc_list:
                self.message_text=each
                if is_word(self.valid_words, self.apply_shift(shift)):
                    d[shift]+=1
        maxi=max(d.values())
        self.message_text=original
        for k in d:
            if d[k]== maxi:
                return (k,self.apply_shift(k))
            
def decrypt_story():
    enc_story=get_story_string()  
    cipher=CiphertextMessage(enc_story)
    return cipher.decrypt_message()
          
            


#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('Opotfotf xpset: tvnnfs tfbu bqqfbsbodf qspufdujpo mfbuifs qbsfou nbobhf iptqjubm gbwpsjuf uijfg hpme qsjdf xjoh qpmjdf sfqmbdf iboh usfbtvsf kpjou bewboubhf mbeefs sfeefo djsdmf mpve mfbtu xfbwf cjdzdmf xblf ipsjapoubm uvcf nfbtvsf hsjoe qmbuf opu sftfswf qsjou')
#print('Expected Output:', (24, 'hello'))
print ('Expected Output:', ('Nonsense'))
print('Actual Output:', ciphertext.decrypt_message())

#Another test case cipherlongtext)
#cipherlong= CiphertextMessage('Fgfkwfkw ogjvk: mkw hdwskw zsfvkzscw tjwslz ozslwnwj wnwjqozwjw wfyafwwj hgwe kdsnw jansd udwnwj nwad zmjjsz khwuasd zsl')
##print ('Expected Output: Nonsense words: like stage collector spoon curl satisfactory abroad crowd tray newspaper drink blood system proof although')
#print ('Message text: ', cipherlong.message_text)
#print ('Actual Output: ', cipherlong.decrypt_message())
#print ('New:',cipherlong.get_message_text())
#
