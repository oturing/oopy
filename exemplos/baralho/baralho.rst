===================
Baralho polimórfico
===================

Instanciar e contar::

  >>> from baralho import Baralho
  >>> b = Baralho()
  >>> len(b)
  52

Acessar cartas::

  >>> b[0]
  Carta('2', 'paus')
  >>> b[-2:]
  [Carta('K', 'espadas'), Carta('A', 'espadas')]
  >>> for carta in b[:3]: print carta
  Carta('2', 'paus')
  Carta('3', 'paus')
  Carta('4', 'paus')

