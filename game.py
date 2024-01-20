import random
from enum import Enum
from typing import List


# from colorama import Back

# recreating colorama functionality so user doesn't have to have it installed + not sure if libraries are allowed for recurse center
# code partially stolen from colorama
class AnsiBack():
    BLACK           = f'\033[{40}m'
    GREEN           = f'\033[{42}m'
    YELLOW          = f'\033[{43}m'
    RESET           = f'\033[{49}m'
    LIGHTBLACK_EX   = f'\033[{100}m' # "fairly well supported, but not part of the standard."
Back = AnsiBack()


class ReadoutValues(Enum):
    exact_match = 1 #"exact_match"
    inexact_match = 2 #"inexact_match"
    no_match = 3 # "no_match"
    unknown = 4


#deprecated
def playGameV1(solution_word, allow_invalid_words=False):
    for i in range(5):
        guess = getGuess(allow_invalid_words)
        
        #find which letters of guess match
        readout = getReadout(guess, solution_word) #TODO replace strings with enums

        # print(readout)
        prettyPrintReadout(guess, readout)
        
        if guess == solution_word:
            print(f"Congratulations! You won in {i+1} guesses")
            return
    print(f"You lose, the word was {solution_word}")






from words import VALID_WORDS_LIST
def getGuess(allow_invalid_words=False, valid_words=VALID_WORDS_LIST, solution_word=None):
    while True:
        guess = input("Enter your guess! ").strip().lower()
        if len(guess) != 5:
            print("invalid length, must be 5")
            continue
        if not isRealWord(guess, valid_words, solution_word) and not allow_invalid_words:
            print("that word is not in our word bank")
            continue
        break
    return guess


def isRealWord(word, valid_words, solution_word=None):
    if word in valid_words:
        return True
    elif word == solution_word: # not currently made use of in our code
        return True
    return False

def getReadout(guess, solution):

    inexact_match_indexes, exact_match_indexes = getMatches(guess, solution)

    readout:list[ReadoutValues] = []
    for i, letter in enumerate(guess):
        if i in exact_match_indexes:
            readout.append(ReadoutValues.exact_match)
        elif i in inexact_match_indexes:
            readout.append(ReadoutValues.inexact_match)
        else:
            readout.append(ReadoutValues.no_match)

    return readout

def getMatches(guess, solution):

    inexact_match_indexes = []
    exact_match_indexes = []
    
    """
        for i, letter in enumerate(guess):
            if (letter in solution): #matches
                if guess[i] == solution[i]: #matches exactly
                    exact_match_indexes.append(i)
                else: # doesn't match exactly
                    # TODO check if its repeated
                    inexact_match_indexes.append(i)
    """

    # put all solution letters in unmatched_solution_letters
    unmatched_solution_letters = {}
    for letter in solution:
        unmatched_solution_letters[letter] = unmatched_solution_letters.get(letter, 0) + 1 #get the current letter, if no current letter get 0
    # print(unmatched_solution_letters)

    #check exact matches (and eliminate from solution_letters)
    for i, letter in enumerate(guess):
        if guess[i] == solution[i]: #matches exactly
            exact_match_indexes.append(i)
            # remove the letter from unmatched_solution_letters
            unmatched_solution_letters[letter] = unmatched_solution_letters.get(letter, 1) - 1
    # print(unmatched_solution_letters)

    # check inexact matches
    for i, letter in enumerate(guess):
        if i in exact_match_indexes: 
            continue

        is_match = unmatched_solution_letters.get(letter, 0) >= 1
        if is_match:
            inexact_match_indexes.append(i)
            # remove the letter from unmatched_solution_letters
            unmatched_solution_letters[letter] = unmatched_solution_letters.get(letter, 1) - 1
    
    # print(unmatched_solution_letters)

    # if solution_letters.get(letter, 0) >= 1:
    #         solution_letters[letter] = solution_letters.get(letter, 1) - 1
        
    # print(inexact_match_indexes, exact_match_indexes)
    return (inexact_match_indexes, exact_match_indexes)

def uglyPrintReadout(guess, readout:List[ReadoutValues]):
    for i,letter in enumerate(guess):
        if readout[i] == ReadoutValues.exact_match:
            print("exact match:", letter)
        elif readout[i] == ReadoutValues.inexact_match:
            print("inexact match", letter)
        else:
            print("no match", letter)

def prettyPrintReadout(guess, readout:List[ReadoutValues]):
    for i,letter in enumerate(guess):
        prettyPrintLetter(letter, readout[i], print_no_match_as_unknown=True)

        # if readout[i] == ReadoutValues.exact_match:
        #     print(Back.GREEN + letter, end="")
        # elif readout[i] == ReadoutValues.inexact_match:
        #     print(Back.YELLOW + letter, end="")
        # else:
        #     print(Back.RESET + letter, end="")

    print(Back.RESET)

def prettyPrintLetter(letter, type:ReadoutValues, print_no_match_as_unknown=False):
    if type == ReadoutValues.exact_match:
        print(Back.GREEN + letter, end="")
    elif type == ReadoutValues.inexact_match:
        print(Back.YELLOW + letter, end="")
    
    elif type == ReadoutValues.no_match and not print_no_match_as_unknown:
        color_code = Back.LIGHTBLACK_EX
        print(color_code + letter, end="")
    
    else:
        print(Back.RESET + letter, end="")
    print(Back.RESET, end="") 