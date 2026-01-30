'''
P: given word return scrabble score, case-insensitive, only
    alphabetic characters count
E: 'a' -> 1
D: none
A: sum generator that scores helper for each character,
    if word is None return 0
    char_value returns score from dictionary with key
    of char.lower() if alpha, otherwise zero
C: below
'''

class Scrabble:
    LETTER_VALUES = {
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10,
    }

    @classmethod
    def _char_value(cls, char):
        if char.isalpha():
            return cls.LETTER_VALUES[char.lower()]
        return 0
    
    @classmethod
    def calculate_score(cls, word):
        if word is None:
            return 0
        return sum(cls._char_value(char) 
                   for char in word)
    
    def __init__(self, word):
        self._word = word

    def score(self):
        return type(self).calculate_score(self._word)