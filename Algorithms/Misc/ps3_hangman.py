# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letters in secretWord:
        if letters not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    guess =[]
    
    for letter in secretWord:
        if letter in lettersGuessed:
            guess.append(letter)
        else:
            guess.append('_')
    
    return " ".join(guess)


import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = []
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available.append(letter)
            
    return "".join(available)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is ", len(secretWord), 'letters long')
    print('-----------')
    tries = 8
    lettersGuessed = []

    # run this loop while secret word is not equal to lettersGuessed

    while isWordGuessed(secretWord, lettersGuessed) == False and tries > 0:
        print("You have ", str(tries), " guesses left")
        guess = input('Please guess a letter: ').lower()
        lettersGuessed.append(guess)

        if guess in secretWord:
            print('Good guess:', guess)
        else:
            tries -= 1
            print('Incorrect')
            print('Number of guesses ', tries)
            
        print(getGuessedWord(secretWord, lettersGuessed))
        print("Available Letters: ", getAvailableLetters(lettersGuessed))
        
        if mistakes == 8:
            return print('Sorry, you ran out of guesses. The word was ', secretWord)

    return print('Congratulations, you won!')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
