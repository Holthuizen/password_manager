import secrets
import random


class Diceware:
    def __init__(self):
        self.wordlist = []
        self.load_wordlist()

    def read_file(self,path): 
        file = open(path, 'r')  # Open file 
        contents = file.read()
        file.close()
        return contents
    def load_wordlist(self): 
        #read wordlist from file, encode to bytes
        words_bytes = self.read_file("diceware_list.txt").encode()
        #remove tabs and split on newline
        _wordlist = words_bytes.replace(b'\t',b'').split(b'\n')
        for pair in _wordlist: 
            #split number from word and only store the word 
           self.wordlist.append(pair[5:].decode())
    def throw(self,n):
        if(n < 3): 
            print(f"{n} is to low of a number")
            exit()
        password = "" 
        divider='*'
        for t in range(n):
            #pick even word with different random method than odd words 
            if(t % 2 == 0):
                password += secrets.choice( self.wordlist ) #picks random item
            else: 
                password += random.choice( self.wordlist ) #picks random item
            password += divider
        return(password[0:len(password)-1])


# return Diceware()