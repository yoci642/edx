"""Hangman game"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    i = 0
    while i < len(secretWord) and secretWord[i] in lettersGuessed:
        i += 1
    if i < len(secretWord):
        return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    i = 0
    while i <len(secretWord):
        if secretWord[i] in lettersGuessed:
            guessedWord += secretWord[i]
        else:
            guessedWord += '_'
        i += 1
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    availableLetters = ''
    for letter in allLetters:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters

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
    # START GAME
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    # INITIALIZE VARIABLES
    guessesLeft = 8
    guessedLetters = ''
    guessedWord = getGuessedWord(secretWord, guessedLetters)
    while guessesLeft > 0 and not isWordGuessed(secretWord, guessedLetters):
        print("You have " + str(guessesLeft) + " guesses left.")
        print("Available letters: " + getAvailableLetters(guessedLetters))
        userGuess = raw_input("Please guess a letter: ").lower()
        if userGuess not in getAvailableLetters(guessedLetters):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters))
        else:
            guessedLetters += userGuess
            if userGuess in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, guessedLetters))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessedLetters))
                guessesLeft -= 1
        print("-------------")

    # END GAME
    if guessesLeft == 0:
        print("Sorry, you ran out of guesses. The word was else.")
    else:
        print("Congratulations, you won!")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = "y" # chooseWord(wordlist).lower()
hangman(secretWord)