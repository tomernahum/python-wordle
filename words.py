
from pathlib import Path
def convertFileToList(filename:str):
	# from pathlib import Path
	p1 = Path(__file__).with_name(filename) #opens file from correct directory. got from stackoverflow
	with p1.open(mode="r") as file:
		out = [line.rstrip('\n') for line in file]
	return out

VALID_WORDS_LIST = convertFileToList("valid_words.txt")
	

# POSSIBLE_SOLUTION_WORDS_LIST = VALID_WORDS_LIST
POSSIBLE_SOLUTION_WORDS_LIST = convertFileToList("possible_solution_words.txt")



LETTERS = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


