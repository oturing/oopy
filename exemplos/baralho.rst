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
  Carta('2', 'espadas')
  >>> b[-2:]
  [Carta('K', 'copas'), Carta('A', 'copas')]
  >>> for carta in b[:3]: print carta
  Carta('2', 'espadas')
  Carta('3', 'espadas')
  Carta('4', 'espadas')

