# coding: utf-8

"""
===========================
Testando um tômbola com bug
===========================

Para começar, vamos criar uma instância de tômbola. Nessa implementação,
é necessário fornecer uma sequência de itens ao construtor::

    >>> from tombola_bug import Tombola
    >>> bolas = [77, 88, 99]
    >>> t = Tombola(bolas)
    >>> t.carregada()
    True

Vamos tirar a última bola::

    >>> t.sortear() # sortear sem misturar devolve o ultimo item colocado
    99

Agora veja o que aconteceu com a lista ``bolas``::

    >>> bolas       #doctest: -SKIP
    [77, 88]

(veja nota no final deste texto para enteder o -SKIP)

Porque isso aconteceu?

Dica: a explicação começa por aqui::

    >>> t.itens is bolas
    True

Isso é um problema porque o usuário da tômbola provavelmente não espera
que itens de sua lista serão descartados durante o uso.

O que deve ser feito para eliminar este problema e fazer o teste a seguir
passar?

    >>> bolas
    [77, 88, 99]

NOTA: Uma vez resolvido este exercício você poderá mudar a diretiva -SKIP
para +SKIP na linha 24 para ignorar aquele teste.


"""

class Tombola(object):
    '''IMPLEMENTACAO COM BUG!!!'''

    def __init__(self, seq):
        self.itens = seq

    def carregar(self, seq):
        self.itens.extend(seq)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)
