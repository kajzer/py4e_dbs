#!/usr/bin/env python3
# hangmanGame.py - hangman game.. what else to say about it?

import random, requests, urllib, json, string

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
       
INTRO_TEXT = '''This is the game Hangman. If You don't know rules check out this URL: https://en.wikipedia.org/wiki/Hangman_(game)
You got seven tries before you HANG!                                                                                              '''
       
# class to colorize some text
class Colorize:
    codes = {
            'green': '\033[1;32;40m',
            'magenta': '\033[0;35;40m',
            'reset_seq': '\033[0m'
    }
    
    @staticmethod
    def text(message, color):
        return Colorize.codes[color] + message + Colorize.codes['reset_seq']    


def getRandomWord(wordList):
    # This function returns a random string from passed list
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]['word']
    
def getWords(letterCount):
    letterCount -= 1
    exlamation_count = '?' * letterCount
    # getting random front letter makes words a lil nicer and allows to limit results from api
    word_code = string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)] + exlamation_count #string.ascii_lowercase
    # get words from api
    url = 'https://api.datamuse.com/words?%s' % (urllib.parse.urlencode({'sp': word_code, 'max': '250'}))
    response = requests.get(url)
    response.raise_for_status()
    # parse json response and return
    words = json.loads(response.text)
    return words
    
def getLetterCount():
    while True:
        try:
            letters = int(input('How many letters should the word have?: '))
            if letters < 4:
                print('That would be to easy!! Try with 4 letter')
                letters = 4
            return letters
        except:
            print('Something went wrong with Your inpu. Please give a number!')
            continue
    

def main():
    print(Colorize.text('================== H A N G M A N ======================', 'green'))
    print(Colorize.text(INTRO_TEXT, 'magenta'))
    missedLetters = ''
    correctLetters = ''
    secretWord = ''
    gameIsDone = False
    
    countL = getLetterCount()
    secretWord = getRandomWord(getWords(countL))
    
    print(secretWord)
    
    
    
if __name__ == "__main__":
    main()