==================================
Tômbola: um dispositivo de sorteio
==================================

A tômbola é um recipiente que acomoda objetos numerados para realizar
sorteios, por exemplo no jogo de bingo. O recipiente pode ser tão diverso quanto um globo ou uma gaiola esférica que gira sobre um eixo, ou um
prisma transparente, ou mesmo simples saco.

Nossa implementação de tômbola em Python pode ser instanciada simplesmente
assim::

  >>> from tombola import Tombola
  >>> t = Tombola()

No entanto, para usá-la é preciso carregar com números (ou qualquer
sequência de objetos)::

  >>> t.carregar(range(3))

Sem misturar, o "sorteio" simplesmente devolve o último item colocado::

  >>> t.sortear()
  2

O método `Tombola.misturar` corresponde a girar a manivela do globo, ou
sacudir bem o saco::

  >>> t.misturar() 
  >>> t.sortear() # doctest:+SKIP
  1

É possível verificar se a tômbola ainda tem itens a sortear::

  >>> t.carregada()
  True

Se tentarmos um sorteio com a tômbola vazia, ocorre uma exceção::

  >>> _ = t.sortear()
  >>> _ = t.sortear()
  >>> _ = t.sortear()
  Traceback (most recent call last):
    ...
  IndexError: pop from empty list

Agora ela não está mais carregada::

  >>> t.carregada()
  False




