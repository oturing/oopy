# coding: utf-8

from math import sqrt

class Vetor(object):
    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
            >>> Vetor(1, 2)
            Vetor(1, 2)
        '''
        return 'Vetor(%s, %s)' % (self.x, self.y)

    def distancia(self, v2):
        '''
            >>> p1 = Vetor(2, 1)
            >>> p2 = Vetor(3, 1)
            >>> p1.distancia(p2) # doctest: +ELLIPSIS
            1.0...

        '''
        dx = self.x - v2.x
        dy = self.y - v2.y
        return sqrt(dx*dx + dy*dy)

    def __abs__(self):
        '''
            >>> abs(Vetor(3, 4)) # doctest: +ELLIPSIS
            5.0...
        '''
        return self.distancia(Vetor(0,0))

    def __add__(self, v2):
        '''
            >>> pos = Vetor(2, 1)
            >>> vel = Vetor(2, 4)
            >>> pos + vel
            Vetor(3, 4)
        '''
        dx = self.x + v2.x
        dy = self.y + v2.y
        return Vetor(dx, dy)

    def __mul__(self, n):
        '''Multiplicação escalar::

            >>> Vetor(2, 1) * 4
            Vetor(8, 4)
        '''
        return Vetor(self.x*n, self.y*n)

if __name__=='__main__':
    import doctest
    doctest.testmod()


