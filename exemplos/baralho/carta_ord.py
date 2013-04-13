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
    Carta('2', 'paus')
    >>> monte[-3:]
    [Carta('Q', 'espadas'), Carta('K', 'espadas'), Carta('A', 'espadas')]

Equivalência::

    >>> as_espadas = Carta('A', 'espadas')
    >>> as_espadas == Carta('A', 'espadas')
    True
    >>> as_espadas != Carta('7', 'ouros')
    True

Ordenação::

    >>> as_copas = Carta('A', 'copas')
    >>> rei = Carta('K', 'espadas')
    >>> dois = Carta('2', 'paus')
    >>> dois.peso
    0
    >>> as_espadas.peso
    51
    >>> as_copas.peso
    50
    >>> rei.peso
    47
    >>> as_copas > dois
    True
    >>> dois > as_copas
    False
    >>> dois < as_copas  # automagico
    True
    >>> dois < as_espadas
    True
    >>> as_copas <= as_espadas  # automagico
    True
    >>> as_copas <= Carta('A', 'copas')  # automagico
    True


Ordenação total::

    >>> dois >= as_espadas
    False

Lucro::

    >>> mao = [as_espadas, dois, as_copas, rei]
    >>> sorted(mao)
    [Carta('2', 'paus'), Carta('K', 'espadas'), Carta('A', 'copas'), Carta('A', 'espadas')]

'''


from functools import total_ordering

@total_ordering
class Carta(object):

    # naipes em ordem crescente conforme o Bridge
    naipes = 'paus ouros copas espadas'.split()
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

    @property
    def peso(self):
        try:
            return self.__peso
        except AttributeError:
            peso_valor = Carta.valores.index(self.valor)
            peso_naipe = Carta.naipes.index(self.naipe)
            self.__peso = peso_valor * len(Carta.naipes) + peso_naipe
            return self.__peso

    def __gt__(self, outra):
        return self.peso > outra.peso
