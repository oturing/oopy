# coding: utf-8

"""
===================================
Testando com injeção de dependência
===================================

A tômbola depende de uma função pseudo-aleatória para funcionar, e isso
dificulta os testes. Para facilitar testes nestes casos é comum usar injeção
de dependência. Isso é pode ser feito acrescentando um parâmetro ao método que
depende da função pseudo-aleatória, permitindo trocar essa dependência por uma
função de resultado previsível.

Neste caso vamos substituir a função ``randrange`` usada em ``sortear`` pela
função ``sorteio_fake``::

    >>> def sorteio_fake(n):
    ...      return n/2

Em nossa tômbola, essa função vai gerar sempre o índice do meio na sequência
(``len(seq)/2``).Para injetar a função, ela é passada como parâmetro nomeado
``randomizador`` para o método ``sortear``::

    >>> t = MiniTombola()
    >>> t.carregar('ABCDE')
    >>> t.sortear(randomizador=sorteio_fake)
    'C'
    >>> t.sortear(randomizador=sorteio_fake)
    'D'
    >>> t.sortear(randomizador=sorteio_fake)
    'B'
    >>> t.sortear(randomizador=sorteio_fake)
    'E'
    >>> t.sortear(randomizador=sorteio_fake)
    'A'

"""

from tombola_abc import TombolaABC

from random import randrange

class MiniTombola(TombolaABC):
    def __init__(self):
        self.itens = []
    def carregar(self, seq):
        self.itens = list(seq)
    def sortear(self, randomizador=None):
        if randomizador is None:
            randomizador = randrange
        pos = randomizador(len(self.itens))
        return self.itens.pop(pos)
    @property
    def carregada(self):
        return bool(self.itens)

if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
