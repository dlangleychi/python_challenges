'''
P: convert arabic number to roman numerals (limit 3000)
E: 1 -> I
D: none
A: make helper for converting one digit taking one, five, ten
    apply to ones digit, //=10 apply to tens, etc
C: below
'''

class RomanNumeral:
    ONE = 'I'
    FIVE = 'V'
    TEN = 'X'
    FIFTY = 'L'
    HUNDRED = 'C'
    FIVE_HUNDRED = 'D'
    THOUSAND = 'M'

    @staticmethod
    def convert_digit(digit, one, five, ten):
        if digit <= 3:
            return one * digit
        if digit == 4:
            return one + five
        if digit <= 8:
            return five + one * (digit - 5)
        if digit == 9:
            return one + ten

    def __init__(self, num):
        self._num = num

    def to_roman(self):
        result = ''
        temp_num = self._num

        # ones digit
        result = RomanNumeral.convert_digit(
            temp_num % 10, RomanNumeral.ONE, 
            RomanNumeral.FIVE, RomanNumeral.TEN)
        temp_num //= 10

        # tens digit
        result = RomanNumeral.convert_digit(
            temp_num % 10, RomanNumeral.TEN, 
            RomanNumeral.FIFTY, RomanNumeral.HUNDRED) + result
        temp_num //= 10

        # hundreds digit
        result = RomanNumeral.convert_digit(
            temp_num % 10, RomanNumeral.HUNDRED, 
            RomanNumeral.FIVE_HUNDRED, RomanNumeral.THOUSAND) + result
        temp_num //= 10

        # thousands digit (don't have to worry about > 3000)
        result = RomanNumeral.convert_digit(
            temp_num % 10, RomanNumeral.THOUSAND, 
            '', '') + result

        return result