==================
Testando a tômbola
==================

Para começar, precisamos criar uma instância de tômbola::

	>>> from tombola import Tombola
	>>> t = Tombola()

Antes de sortear, é preciso carregar::

	>>> t.carregar([1, 2, 3])

Agora, podemos sortear::

	>>> res = t.sortear()
	>>> res in [1, 2, 3]
	True

Podemos verificar se a tombola está carregada (se tem alguma bola)::

	>>> t.carregada()
	True
	>>> _ = t.sortear()
	>>> _ = t.sortear()
	>>> t.carregada()
	False
	




