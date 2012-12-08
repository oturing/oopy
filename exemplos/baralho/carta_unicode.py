#/usr/bin/env python3
# este programa só funciona em Python 3 pois depende de strings Unicode
# e assume que o encoding padrão do código-fonte é UTF-8

'''
Classe que representa cartas de baralho

    >>> zape = Carta('4', 'paus')
    >>> zape.valor
    '4'
    >>> zape
    Carta('4', 'paus')
    >>> print(zape)
    4♣

Método da classe::

    >>> monte = Carta.todas()
    >>> len(monte)
    52
    >>> monte[0]
    Carta('2', 'paus')
    >>> monte[-3:]
    [Carta('Q', 'espadas'), Carta('K', 'espadas'), Carta('A', 'espadas')]
    >>> for carta in reversed(monte[-3:]):
    ...     print(carta)
    A♠
    K♠
    Q♠

'''

class Carta(object):

    # naipes em ordem crescente conforme o Bridge
    naipes = 'paus ouros copas espadas'.split()
    valores = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    simbolos = dict(zip(naipes, '♣♦♥♠'))

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return 'Carta(%r, %r)' % (self.valor, self.naipe)

    def __str__(self):
        return self.valor + Carta.simbolos[self.naipe]

    @classmethod
    def todas(cls):
        return [cls(v, n) for n in cls.naipes
                          for v in cls.valores]
