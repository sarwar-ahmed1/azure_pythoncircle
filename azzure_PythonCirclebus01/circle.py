'''Circle class for cohort CE05!'''
import math


class Circle:
    '''Circle to represent circle'''

    def __init__(self, radius: float):
        '''Circle constructor'''
        if radius <= 0.0:
            raise ValueError('Radius must be greater than 0.0')
        self.radius = radius

    def area(self):
        '''Area access method'''
        return math.pi*self.radius**2

    def perimeter(self):  # pylint: disable=C0116
        return 2 * math.pi * self.radius

    def summary(self):  # pylint: disable=C0116
        area2dp = round(self.area(), 2)
        perimeter2dp = round(self.perimeter(), 2)
        return f'The area is {area2dp} and the perimeter is {perimeter2dp}'