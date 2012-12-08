# coding: utf-8

'''
Classe que representa cartas de baralho

    >>> zape = Carta('4', 'paus')
    >>> zape.valor
    '4'
    >>> zape
    Carta('4', 'paus')

Método da classe::

    >>> monte = Carta.todas()
    >>> len(monte)
    52
    >>> monte[0]
    Carta('2', 'espadas')
    >>> monte[-3:]
    [Carta('Q', 'copas'), Carta('K', 'copas'), Carta('A', 'copas')]

Ordenação::

    >>> as_ = Carta('A', 'copas')
    >>> rei = Carta('K', 'copas')
    >>> dois = Carta('2', 'espadas')
    >>> dois.peso()
    0
    >>> as_.peso()
    51
    >>> rei.peso()
    50
    >>> as_ > dois
    True
    >>> dois > as_
    False
    >>> dois < as_  # automagico
    True


Equivalência::

    >>> as_ == Carta('A', 'copas')
    True
    >>> as_ != dois
    True


Ordenação total::

    >>> Carta('A', 'copas') >= as_
    True
    >>> dois >= as_
    False
    >>> dois <= as_
    True

Lucro::

    >>> mao = [dois, as_, rei]
    >>> sorted(mao)
    [Carta('2', 'espadas'), Carta('K', 'copas'), Carta('A', 'copas')]

'''


from functools import total_ordering

@total_ordering
class Carta(object):

    naipes = 'espadas ouros paus copas'.split()
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return 'Carta(%r, %r)' % (self.valor, self.naipe)

    @classmethod
    def todas(cls):
        return [cls(v, n) for n in cls.naipes
                          for v in cls.valores]

    def __eq__(self, outra):
        return ((self.valor, self.naipe) ==
                (outra.valor, outra.naipe))

    def peso(self):
        return (Carta.valores.index(self.valor) +
            len(Carta.valores) * Carta.naipes.index(self.naipe))

    def __gt__(self, outra):
        return self.peso() > outra.peso()
