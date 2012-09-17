# coding: utf-8

"""
================================
Testando a outra tômbola com bug
================================

Para começar, vamos criar uma instância de tômbola com uma sequência de
itens::

    >>> bolas = [77, 88, 99]
    >>> t = Tombola(bolas)
    >>> t.carregada()
    True

Vamos tirar a última bola::

    >>> t.sortear() # sortear sem embaralhar devolve o ultimo item colocado
    99

Agora vamos criar uma nova tômbola ``t2``::

    >>> t2 = Tombola()

Neste caso, ``t`` e ``t2`` não compartilham os itens::

    >>> t2.carregada()
    False

Porém, veja o que aconteceu com a lista ``bolas``::

    >>> bolas
    [77, 88]

Além disso, se carregarmos os a tômbola depois de instanciada, aconteceu
o seguinte::

    >>> t2.carregar([18, 19])
    >>> t3 = Tombola()
    >>> t3.carregada()
    True

A explicação começa por aqui::

    >>> t2.itens is t3.itens
    True

Porém::

    >>> t2.itens is t.itens
    False

Por quê?

"""

class Tombola(object):
    '''IMPLEMENTACAO COM BUG!!!'''

    def __init__(self, seq=[]):
        self.itens = seq

    def carregar(self, seq):
        self.itens.extend(seq)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)
