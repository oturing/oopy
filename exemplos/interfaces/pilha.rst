==================
Tesde de uma pilha
==================

A pilha é um tipo de dado abstrato que segue a regra LIFO (last in, first out;
último a entrar, primeiro a sair). A interface básica de uma pilha define duas
operações: push (colocar) e pop (retirar)::

    >>> from pilha import PilhaSimples
    >>> p = PilhaSimples()
    >>> p.colocar(7)
    >>> p.retirar()
    7
    >>> p.colocar(10)
    >>> p.colocar(20)
    >>> p.colocar(30)
    >>> p.retirar()
    30
    >>> p.retirar()
    20
    >>> p.retirar()
    10

Uso incorreto
-------------

Tentar retirar um item quando a pilha está vazia produz uma exceção::

    >>> p.retirar()
    Traceback (most recent call last):
        ...
    LookupError: pilha vazia
