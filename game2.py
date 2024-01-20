from typing import List

from game import getGuess, getReadout, prettyPrintReadout, getMatches, ReadoutValues, prettyPrintLetter
from words import LETTERS



class Guess:
    def __init__(self, guess_word, solution_word) -> None:
        self.word = guess_word
        self.readout = getReadout(guess_word, solution_word)
    
    def prettyPrintReadout(self):
        prettyPrintReadout(self.word, self.readout)


from words import VALID_WORDS_LIST
def playGameV2(solution_word, valid_words=VALID_WORDS_LIST, allow_invalid_words=False, spoil=False, clearScreen=True):

    past_guesses = []
    letters_knowledge = {}

    if clearScreen:
        printScreen(past_guesses, letters_knowledge, overwrite=True)
    for i in range(5):
        if spoil and i==0: print("solution word:", solution_word)
        
        guess_word = getGuess(allow_invalid_words)
        
        guess = Guess(guess_word, solution_word)
        updateLettersKnowledge(guess.word, solution_word, letters_knowledge)
        
        past_guesses.append(guess)
        printScreen(past_guesses, letters_knowledge, overwrite=clearScreen)
        
        if guess.word == solution_word:
            print(f"Congratulations! You won in {i+1} guesses")
            return
        

    print(f"You lose, the word was {solution_word}")

def updateLettersKnowledge(guess_word, solution_word, letters_knowledge:dict):
    inexact_match_indexes, exact_match_indexes = getMatches(guess_word, solution_word)

    for i, letter in enumerate(guess_word):
        letter_found_previously = letters_knowledge.get(letter) == ReadoutValues.exact_match
        if letter_found_previously:
            continue

        if i in exact_match_indexes:
            letters_knowledge[letter] = ReadoutValues.exact_match
        elif i in inexact_match_indexes:
            letters_knowledge[letter] = ReadoutValues.inexact_match
        else:
            letters_knowledge[letter] = ReadoutValues.no_match


def printScreen(guesses:List[Guess], letters_knowledge:dict, overwrite=True):
    if overwrite:
        # print("\033[2J")
        # print("\033[H")
        # print("\033c")
        import os
        os.system('clear')
        

    print("")
    for guess in guesses:
        guess.prettyPrintReadout()
    for i in range(5 - len(guesses)):
        # print("_____")
        print("-----")
    
    print("")
    printKeyboard(letters_knowledge)
    print("")

def printKeyboard(letters_knowledge:"dict[str,ReadoutValues]", mode=2):
    
    if mode == 1:
        for letter in LETTERS:
            letter_readout = letters_knowledge.get(letter, ReadoutValues.unknown)
            prettyPrintLetter(letter.upper(), letter_readout, print_no_match_as_unknown=False)
        print("") # new line

    else:
        KEYBOARD_LETTERS = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ] #thx chatgpt
        for row in KEYBOARD_LETTERS:
            for letter in row:
                letter_readout = letters_knowledge.get(letter.lower(), ReadoutValues.unknown)
                prettyPrintLetter(letter.upper(), letter_readout, print_no_match_as_unknown=False)
            print("") # new line
    

