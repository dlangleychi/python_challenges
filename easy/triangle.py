class Triangle:
    EQUILATERAL = 'equilateral'
    ISOSCELES = 'isosceles'
    SCALENE = 'scalene'
    
    def __init__(self, a, b, c):
        self._a, self._b, self._c = sorted([a, b, c])

        if self._a <= 0:
            raise ValueError('All sides must be > 0.')

        if self._a + self._b <= self._c:
            raise ValueError(
                'Sum of smaller sides must be greater than larger side.'
                )
        
    @property
    def kind(self):
        if self._a == self._b == self._c:
            return Triangle.EQUILATERAL
        
        if self._a == self._b or self._b == self._c:
            return Triangle.ISOSCELES
        
        return Triangle.SCALENE
    