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
            'red': '\033[0;31;40m',
            'blue': '\033[0;34;40m',
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
            print(Colorize.text('Something went wrong with Your inpu. Please give a number!', 'red'))
            continue

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    # replace blanks with guessed correct letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    # show secret word with spaces in between
    print('Your word:', end=' ')
    for letter in blanks:
        print(letter, end=' ')
    print()
    
def getGuess(allreadyGuessed):
    # returnes the letter the player entered
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if guess not in string.ascii_letters:
            print(Colorize.text('Please fill in a letter!', 'red'))
            continue
        elif guess in allreadyGuessed:
            print(Colorize.text('You have allready guessed that letter. Choose again', 'blue'))
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again otherwise false
    return input('Do you want to play again? (yes or no) ').lower().startswith('y')
    

def main():
    print(Colorize.text('================== H A N G M A N ======================', 'green'))
    print(Colorize.text(INTRO_TEXT, 'magenta'))
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False
    
    countL = getLetterCount()
    secretWord = getRandomWord(getWords(countL))
    
    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        # get guess from a user
        guess = getGuess(missedLetters + correctLetters)
        
        if guess in secretWord:
            correctLetters += guess
            # check if player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            
            # check if player has guessed to manny times and lost.
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True
        
        # Ask the player if they want to play again but only if the game is done
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                
                countL = getLetterCount()
                secretWord = getRandomWord(getWords(countL))
            else:
                break
    
    
if __name__ == "__main__":
    main()