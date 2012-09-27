# coding: utf-8

"""
============================
Testando uma classe abstrata
============================

Uma classe abstrata não pode ser instanciada::

    >>> a = TombolaABC()  #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      ...
    TypeError: Can't instantiate abstract class...

Os detalhes da exceção que foram omitidos acima mencionam todos os métodos
(e propriedades) abstratos:

    Can't instantiate abstract class TombolaABC with abstract methods
    carregada, carregar, sortear

Ao final deste módulo, implementamos uma subclasse concreta de ``Tombola``.
Testando essa implementação::

    >>> t = MiniTombola()
    >>> t.carregada
    False
    >>> bolas = {1, 2, 3}
    >>> t.carregar(bolas)
    >>> t.carregada
    True

Agora vamos sortear alguns itens, verificando se estão sendo retirados da
tômbola, e também retirando os itens sorteados da nossa coleção de
controle::

    >>> res = t.sortear()
    >>> res in bolas
    True
    >>> bolas.remove(res)

Repetindo o processo::

    >>> res = t.sortear()
    >>> res in bolas
    True
    >>> bolas.remove(res)

Mais uma vez::

    >>> res = t.sortear()
    >>> res in bolas
    True
    >>> bolas.remove(res)

Agora a tômbola está vazia e não sobraram mais bolas na coleção de
controle::

    >>> len(bolas)
    0
    >>> t.carregada
    False


"""

from tombola_abc import TombolaABC

from random import randrange

class MiniTombola(TombolaABC):
    def __init__(self):
        self.itens = []
    def carregar(self, seq):
        self.itens = list(seq)
    def sortear(self, randomizador=None):
        pos = randrange(len(self.itens))
        return self.itens.pop(pos)
    @property
    def carregada(self):
        return bool(self.itens)

if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
