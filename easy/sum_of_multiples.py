'''
P: given a number and an optional set of numbers 
    (default 3 and 5), return the sum of the multiples of the
    set that are less than the first number
    duplicate multiples are only added once
E: 15, {4, 6} -> 30
D: set for storing multiples
A: multiples is empty set
    for number in set:
        update multiples with range of mutliples of number
            less than first number
    return sum multiples
C: below
'''

class SumOfMultiples:
    DEFAULT_SET = set([3, 5])

    def __init__(self, *args):
        self._nums = set(args) or type(self).DEFAULT_SET

    @staticmethod
    def _find_sum(upper_bound, nums):
        multiples = set()
        for num in nums:
            multiples.update(range(num, upper_bound, num))
        return sum(multiples)
    
    @classmethod
    def sum_up_to(cls, upper_bound):
        return cls._find_sum(
            upper_bound, cls.DEFAULT_SET)
    
    def to(self, upper_bound):
        return self._find_sum(upper_bound, self._nums)