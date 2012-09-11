===================
Exemplos de Doctest
===================

A tipagem dinânica do Python permite aproveitar de um extremo
o conceito de polimorfismo. Veja esta função::

  >>> def dobro(n):
  ...   return n*2

Esta função pode ser usada para 'dobrar' números de qualquer tipo::

  >>> dobro(7)
  14
  >>> dobro(3.1)
  6.2
  >>> dobro(range(1000)) #doctest: +ELLIPSIS
  [0, 1, 2, ..., 998, 999]

Nem sempre é prático ou viável testar::

  >>> from random import randrange
  >>> randrange(100) #doctest: +SKIP
