================================================================
Lista 1: Contador e derivações: um exercício de herança múltipla
================================================================

.. contents:: Sumário

Introdução
==========

Nestes exercícios você fará modificações na classe ``Tombola`` apresentada
durante o curso, aplicando seus conhecimentos sobre iteradores, referências
e propriedades.

Material necessário
-------------------

Além do interpretador Python e seu editor favorito, você vai precisar de três
arquivos que estão no diretório `exercicios/tombola`_ no repositório
`oturing/oopy`_ no GitHub:

* ``tombola.rst``: este arquivo que você está lendo agora, com instruções e
  ``doctests;

* ``tombola.py``: o ponto de partida do exercício; copie e edite sua cópia
  local deste arquivo;

* ``tombola_bug.py``: uma implementação da tômbola com uma falha que você
  deverá diagnosticar e consertar; copie e edite sua cópia local deste
  arquivo;

* ``testar_doc.py``: um script para executar doctests parando na primeira
  falha; bom para orientar a solução do problema passo a passo;

.. _exercicios/tombola: https://github.com/oturing/oopy/tree/master/exercicios/tombola

.. _oturing/oopy: https://github.com/oturing/oopy


Testando a tômbola básica
=========================

Para começar, vamos testar a implementação básica da tômbola, cujo código está em
`exercicios/tombola`_
precisamos criar uma instância de tômbola::

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





