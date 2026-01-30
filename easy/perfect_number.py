'''
P: given number classify it a perfect, deficient or abundant
    don't allow <= 0
E: 6 -> 'perfect'
D: list for factors
A: make helper that calculates that returns the unique factors
    make helper that returns the aliquot sum
    classify based on aliquot sum
C: below
'''

from math import sqrt

class PerfectNumber:
    PERFECT = 'perfect'
    DEFICIENT = 'deficient'
    ABUNDANT = 'abundant'

    @staticmethod
    def _divisors(num):
        if num == 1:
            return []
        
        divisors = set([1])
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num//i)
        return sorted(divisors)
    
    @staticmethod
    def _aliquot_sum(num):
        return sum(PerfectNumber._divisors(num))

    @staticmethod
    def classify(num):
        if num <= 0:
            raise ValueError("Input must be a positive integer")

        aliquot_sum = PerfectNumber._aliquot_sum(num)
        if aliquot_sum < num:
            return PerfectNumber.DEFICIENT
        if aliquot_sum > num:
            return PerfectNumber.ABUNDANT
        return PerfectNumber.PERFECT