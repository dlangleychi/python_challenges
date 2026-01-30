'''
P: given an octal string return a decimal integer,
    invalid or negative result in zero
E: '11' -> 9
D: none
A: make valid digits helper
    result = 0
    for char in input:
        if not valid digit:
            return 0
        result = result * 8 + int(char)
    return result
C: below
'''

class Octal:
    def __init__(self, octal_str):
        self._octal_str = octal_str

    @staticmethod
    def _valid_octal_digit(char):
        return char.isdigit() and (char != '8') and (char != '9')

    def to_decimal(self):
        result = 0
        for char in self._octal_str:
            if not type(self)._valid_octal_digit(char):
                return 0
            result = 8 * result + int(char)

        return result