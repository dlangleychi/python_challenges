class DNA:
    def __init__(self, sequence):
        self._sequence = sequence

    def hamming_distance(self, other_sequence):
        return sum(a != b for a, b 
                   in zip(self._sequence, other_sequence))
