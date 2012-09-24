==========================================
Lista 2: Variações sobre o tema da tômbola
==========================================

.. contents:: Sumário

Introdução
==========

Nestes exercícios você fará modificações na classe ``Tombola`` apresentada
durante o curso, aplicando seus conhecimentos sobre iteradores e referências.

Material necessário
-------------------

Além do interpretador Python e seu editor favorito, você vai precisar de três
arquivos que estão no diretório `exercicios/tombola`_ no repositório
`oturing/oopy`_ no GitHub:

* ``tombola.rst``: este arquivo que você está lendo agora, com instruções e
  ``doctests;

* ``tombola.py``: o ponto de partida do exercício; copie e edite sua cópia
  local deste arquivo;

* ``testar_doc.py``: um script para executar doctests parando na primeira
  falha; bom para orientar a solução do problema passo a passo;

* ``tombola_bug.py``: uma implementação da tômbola com uma falha que você
  deverá diagnosticar e consertar; copie e edite sua cópia local deste
  arquivo;

* ``tombola_bonus.rst``: uma questão mais avançada, para você considerar
  depois que tiver terminado esta lista (se sobrar tempo);

.. _exercicios/tombola: https://github.com/oturing/oopy/tree/master/exercicios/tombola

.. _oturing/oopy: https://github.com/oturing/oopy


2.0 Testando a tômbola básica
=============================

Para começar, vamos testar a implementação básica da tômbola, cujo código está em
`exercicios/tombola/tombola.py`_.

Criamos e carregamos uma instância de tômbola::

    >>> from tombola import Tombola
    >>> t = Tombola()
    >>> bolas = [1, 2, 3]
    >>> t.carregar(bolas)

Agora, podemos sortear::

    >>> res = t.sortear()
    >>> res in bolas
    True

Podemos verificar se a tombola está carregada (se tem alguma bola)::

    >>> t.carregada()
    True
    >>> _ = t.sortear()
    >>> _ = t.sortear()
    >>> t.carregada()
    False

Nos testes acima, usamos a variável ``_`` para receber um valor que queremos
ignorar (do contrário apareceria na saída do console, e o doctest esperaria
o mesmo resultado; porém são resultados que não podemos prever).

Execute os testes deste arquivo agora. Todos os testes acima devem passar.

.. _exercicios/tombola/tombola.py: https://github.com/oturing/oopy/blob/master/exercicios/tombola/tombola.py

2.1. Injeção de dependência para facilitar testes
=================================================

O que é injeção de dependência
------------------------------

Neste exercício veremos como podemos usar a técnica de injeção de dependência
para facilitar testes automatizados.

No caso, o que faremos é substituir a função ``shuffle`` do método
``misturar``, por uma outra função de resultado previsível, simplificando
nossos testes.

A substituição é feita feita pela passagem de um parâmetro, conforme a técnica
da injeção da dependência. Neste caso a "dependência" é a função ``shuffle``,
pois o método ``misturar`` depende dessa função. Em vez de usar sempre a mesma
função ``shuffle``, vamos "injetar" uma implementação falsificada (*fake*) de
``shuffle``.

Procedimento
------------

Voltando à implementação original da classe ``Tombola`` (aquela do item 2.0),
acrescente ao método ``misturar`` um segundo parâmetro formal (depois do
``self``) chamado ``misturadora``, com valor default ``None``.

No corpo do método implemente um teste: se ``misturadora`` for ``None``, use a
função ``random.shuffle`` para misturar os itens da tômbola. Do contrário, use
a função que foi passada como argumento.

Para facilitar o seu trabalho, no módulo `inplace.py`_ você encontrará uma função
``pairswap`` que pode ser usada no lugar de ``shuffle``::

    >>> from inplace import pairswap
    >>> l = [1, 2, 3, 4]
    >>> pairswap(l)
    >>> l
    [2, 1, 4, 3]

Note que, em vez de embaralhar nossa função fake apenas troca cada item em uma
posição par pelo item da posição ímpar seguinte. Note também que a função
``pairswap`` opera modificando a sequência *in-place*, ou seja, ela manipula
os itens da própria sequência passada como argumento, e devolve ``None``. Em
geral, funções em Python que operam *in-place* devolvem ``None`` como uma
maneira de lembrar ao programador que ela modifica o próprio objeto e não cria
um novo.

.. _inplace.py: https://github.com/oturing/oopy/blob/master/exercicios/tombola/inplace.py


Quando seu exercício estiver pronto, esses testes deverão passar::

    >>> bolas = [10, 20, 30, 40]
    >>> t = Tombola()
    >>> t.carregar(bolas)
    >>> t.misturar(pairswap)
    >>> t.sortear()
    30
    >>> t.sortear()
    40
    >>> t.sortear()
    10
    >>> t.sortear()
    20

Note que os itens deverão ser devolvidos na ordem ``[30, 40, 10, 20]`` que é
o inverso da ordem em que foram carregados, porém com os pares trocados.

2.2. Tômbola iterável
=====================

Implemente na tômbola modificada pelo exercício 2.1 a interface **Iterable**.
Relembrando: basta implementar o um método de instância ``__iter__`` que
devolva um iterador ou um gerador.

Repare fizemos a injeção de dependência no exercício 2.1 exatamente para
facilitar os testes neste exercício.

Ao concluir este exercício, este teste deverá passar::

    >>> bolas = [10, 20, 30, 40]
    >>> t = Tombola()
    >>> t.carregar(bolas)
    >>> t.misturar(pairswap)
    >>> for i in t:
    ...    print i
    30
    40
    10
    20

Bônus
-----

(Esta é uma questão avançada, não se sinta mal se não tiver tempo para
resolvê-la.)

Leia o texto do arquivo ``tombola_bonus.rst`` e responda à questão colocada.

2.3. Uma tômbola com um defeito sutil
====================================

No arquivo `exercicios/tombola/tombola_bug.py`_ há uma implementação de
tômbola com método ``__init__`` que permite carregar a tômbola com itens
no momento da instanciação. O módulo ``tombola_bug`` contém doctests
embutidos. Use o comanto ``python -m doctest tombola_bug.py`` para executar
os testes, depois leia o texto e o código para resolver o problema proposto.

.. _exercicios/tombola/tombola_bug.py: https://github.com/oturing/oopy/blob/master/exercicios/tombola/tombola.py

