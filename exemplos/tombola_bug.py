# coding: utf-8

"""
==========================
Testando a tômbola com bug
==========================

Para começar, vamos criar uma instância de tômbola e carregá-la com uma
sequencia de itens::

    >>> t = Tombola()
    >>> t.carregar([11, 22, 33])

Vamos tirar a última bola (sortear sem embaralhar devolve o ultimo item
colocado)::

    >>> t.sortear()
    33

Agora vamos criar uma nova tômbola ``t2``::

    >>> t2 = Tombola()

Neste caso, ``t`` e ``t2`` não compartilham os itens::

    >>> t2.carregada()
    True

O que tem nessa tômbola?

    >>> t2.sortear()
    22
    >>> t2.sortear()
    11

Obviamente tem o os itens da tômbola ``t``... Porquê isso aconteceu?
"""

class Tombola(object):
    '''IMPLEMENTACAO COM BUG!!!'''

    itens = []

    def carregar(self, seq):
        self.itens.extend(seq)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)
