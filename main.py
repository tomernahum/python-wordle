import random
from game import playGameV1
from game2 import playGameV2
from typing import Union, List

from words import POSSIBLE_SOLUTION_WORDS_LIST, VALID_WORDS_LIST

# TODO: maybe export this as a module in __init__.py
# TODO: python docs says its better to use Sequence or Iterable rather than list for typing
def play_game_complete(
    solution_word:Union[str, None]=None, harder_words_mode=False, allow_invalid_words=False, spoil_game=False,
    clear_screen=True,
    valid_words_list:List[str] = VALID_WORDS_LIST, possible_solution_words_list:List[str] = POSSIBLE_SOLUTION_WORDS_LIST,
):
    
    if solution_word != None:
        pass
    elif harder_words_mode:
        solution_word = random.choice(valid_words_list)
    else:
        solution_word = random.choice(possible_solution_words_list)
    
    # TODO: Maybe instead of having all these params passed down over and over they should be grouped into one config object (or maybe two) 
    playGameV2(solution_word, valid_words_list, allow_invalid_words, spoil_game, clear_screen)
    





def main():
    try:
        from colorama import just_fix_windows_console 
        just_fix_windows_console()
        #should make ansi escape sequences (used here for background colors) be compatible with windows. 
        #if they don't have the package installed then just keep working
    except:
        pass


    quick_start = convert_answer_to_bool(input("QuickStart? (y/n) "), default=True)
    if quick_start:
        print("")
        # play_game_complete(allow_invalid_words=True, spoil_game=True)
        play_game_complete(harder_words_mode=False)
        return

    solution_word = None
    # harder_words_mode
    
    # config questions
    pick_word = convert_answer_to_bool(input("Pick your own word? (y/n) "), default=False)
    if pick_word:
        harder_words_mode = False
        spoil_game = False
        solution_word = input("Solution Word: ").strip().lower()
    else:
        spoil_game = convert_answer_to_bool(input("Spoil the game? (y/n) "), default=False)
        harder_words_mode = convert_answer_to_bool(input("Harder Words Mode? (y/n) "), default=False)
    
    allow_invalid_words = convert_answer_to_bool(input("Allow invalid words as guesses? (y/n) "), default=False)
        
    
    clear_screen = convert_answer_to_bool(input("ClearScreen Mode? (y/n) "), default=True)
    # TODO: option for must use found letters from previous guess
    
    # play game
    print("")
    play_game_complete(solution_word, harder_words_mode, allow_invalid_words, spoil_game, clear_screen) 

def convert_answer_to_bool(ans:str, default=None):
    ans = ans.strip().lower()
    if ans in {"y", "yes", "1", "t"}:
        return True
    elif ans in {"n", "no", "0", "f"}:
        return False
    else:
        if default == None:
            raise ValueError("Could not convert answer to boolean")
        else:
            return default


if __name__ == "__main__":
    main()