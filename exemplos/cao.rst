=============
Tipos de Cães
=============

O módulo ``cao.py`` define a classe didática ``Cao`` e algumas subclasses.

	>>> from cao import Cao

Um cão deve ser instanciado com um nome::

	>>> rex = Cao('Rex')

A representação em string de um cão para efeito de inspeção e depuração,
por exemplo, ``repr(rex)``, reproduz a invocação do construtor da classe
``Cao``::

	>>> rex
	Cao('Rex')
	>>> repr(rex)
	"Cao('Rex')"


A representação em string "amigável", para exibição para usuários, é
simplesmente o nome do cão::

	>>> str(rex)
	'Rex'
	>>> print rex
	Rex

Os cães latem, essa é a sua principal função na sociedade::

	>>> rex.latir()
	Rex: Au!
	>>> rex.latir(2)
	Rex: Au! Au!

Quando nervoso, o cão late duas vezes mais::

	>>> rex.nervoso = True
	>>> rex.latir()
	Rex: Au! Au!
	>>> rex.latir(3)
	Rex: Au! Au! Au! Au! Au! Au!

Os cães por padrão não são nervosos, e têm 4 patas. Esses atributos são
definidos na classe, e podem ser acessados através das instâncias::

	>>> rex.qt_patas
	4

Note que a atribuição ``rex.nervoso = True``, feita anteriormente, **não**
modifica o atributo da classe. A atribuição cria um novo atributo de nome
igual, na instância específica onde foi feita a atribuição::

	>>> rex.nervoso
	True

Podemos comprovar que o atributo da classe não mudou acessando-o diretamente::

	>>> Cao.nervoso
	False

Por isso, novos cães continuam nascendo calmos, e não nervosos::

	>>> fido = Cao('Fido ')
	>>> fido.nervoso
	False

Da mesma forma, se o Fido sofrer um acidente isso não vai afetar o Rex,
nem a classe cão::

	>>> fido.qt_patas = 3
	>>> fido.qt_patas
	3

Vale notar que é possível criar novos atributos nas instâncias a qualquer
momento (embora isso nem sempre seja uma boa idéia)::

	>>> rex.peso = 27

Claro que isso não afeta a classe, e muito menos as demais instâncias::

	>>> fido.peso
	Traceback (most recent call last):
	  ...
	AttributeError: 'Cao' object has no attribute 'peso'
