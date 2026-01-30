'''
P: given a number string and a number
    if number is greater than length of string raise ValueError
    return all possible slices of consecutive digit of the length
    return them in a list of lists of ints
E: '123', 3 -> [[1], [2], [3]]
D: list for result
A: if len slice > len string:
    raise ValueError
    result = []
    for i in range(len(string) - number + 1):
        result.append(list(map(int, string[i: i+number])))
    return result (do as comprehension)
C: below
'''

class Series:
    def __init__(self, digit_string):
        self._digit_string = digit_string
        self._len = len(self._digit_string)

    def _slice_list_at(self, start, slice_len):
        return [int(digit) 
                for digit in self._digit_string[start: start + slice_len]]

    def slices(self, slice_len):
        if slice_len > self._len:
            raise ValueError(
                'slice length cannot be greater than digit string length')
    
        return [self._slice_list_at(start, slice_len)
                for start in range(self._len - slice_len + 1)]