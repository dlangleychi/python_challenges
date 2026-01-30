class Anagram:
    @staticmethod
    def _make_key(word):
        return ''.join(sorted(word.lower()))

    def __init__(self, word):
        self._lower_word = word.lower()
        self._key = self.__class__._make_key(word)

    def match(self, word_list):
        return [word for word in word_list 
                if self.__class__._make_key(word) == self._key
                and word.lower() != self._lower_word]
    