================================================================
Lista 1: Contador e derivações: um exercício de herança múltipla
================================================================

.. contents:: Sumário

Introdução
==========

Este exercício é baseado em um exemplo de uso de herança múltipla que aparece
no livro "Internet Programming with Python", de Aaron Watters, Guido van
Rossum e James C. Ahlstrom, publicado em 1996.

Quem já assistiu à palesta "OO em Python sem sotaque" já viu este exemplo
desenvolvido. Mas neste exercício, você fará o desenvolvimento, guiado pelos
testes deste documento.

.. tip:: Funcionalidade existente na biblioteca padrão

    Atualmente o código deste exemplo serve apenas para fins didáticos,
    porque a partir do Python 2.7 já existe na biblioteca padrão a classe
    `collections.Counter`_, que implementa uma funcionalidade muito parecida,
    com uma interface de dicionário.

.. _collections.Counter: http://docs.python.org/library/collections.html#collections.Counter

Material necessário
-------------------

Além do interpretador Python e seu editor favorito, você vai precisar de
três arquivos que estão no diretório `exercicios/contador`_ no repositório `pythonprobr/oopy`_ no GitHub:

* ``contador.rst``: este arquivo que você está lendo agora; ele contém
  doctests além de instruções;

* ``contador.py``: o ponto de partida do exercício; copie e edite sua cópia
  local deste arquivo;

* ``testar_doc.py``: um script para executar os testes do ``contador.rst``
  parando na primeira falha; útil para orientar a solução do problema passo a
  passo;

.. _exercicios/contador: https://github.com/pythonprobr/oopy/tree/master/exercicios/contador

.. pythonprobr/oopy: https://github.com/pythonprobr/oopy

Procedimento
------------

Rode os testes deste arquivo ``contador.rst``. Neste exercício, inicialmente
muitos testes estão falhando, mas não por causa de bugs, e sim porque a
funcionalidade necessária não foi implementada. Sua missão é implementar o
que for preciso para fazer todos os testes passarem.

Recomendo usar o script ``testar_doc.py``, encontrado no diretório
``exercicios`` do repositório ``oopy`` para executar os testes deste arquivo
durante a elaboração do exercício. O ``testar_doc.py`` exibe apenas o
diagnóstico da primeira falha encontrada, facitando o desenvolvimento da
solução passo a passo.

Para executar os testes deste arquivo com o ``testar_doc.py``, faça assim::

    $ python testar_doc.py contador.rst

Dica: na prática, eu costumo incluir um comando ``clear`` para limpar a tela
do shell antes de rodar os testes, assim::

    $ clear; python testar_doc.py contador.rst

No Windows, isso deve funcionar usando ``cls`` em vez de ``clear``, desde que
o caminho até o executável ``python`` esteja no seu ``PATH`` (os instaladores
de Python da ActiveState fazem essa gentileza para você automaticamente).

Uma outra opção, se você estiver utilizando um Linux ou MacOS X é utilizar o 
comando "watch" para ter um feedback constante no terminal:

    $ watch python testar_doc.py contador.rst


Em caso de dúvidas, escreva para o `grupo de discussão Oficinas Turing`_.

.. _grupo de discussão Oficinas Turing: http://goo.gl/uABXr

Dicas de implementação
----------------------

Ao resolver estes exercícios, dedique alguns minutos a pensar como você
implementaria cada solução antes de ler as dicas de implementação.

Se você encontrar uma forma melhor de implementar, ou quiser discutir
alternativas, mande suas idéias para o `grupo de discussão Oficinas
Turing`_.

Extra
-----

Alguns exercícios têm uma seção intitulada **Extra** com sugestões de
atividades adicionais para você fazer, se quiser e puder.


Bom trabalho!

--LR

Exercício 1.1: um contador genérico de ocorrências
==================================================

Neste primeiro exercício você não vai escrever código Python: vai apenas ler o
código de uma classe que será o nosso ponto de partida, e também configurar o
seu ambiente para rodar os doctests deste arquivo que você está lendo agora.

O módulo `contador.py`_ contém a implementação de uma classe ``Contador``.

.. _contador.py: https://github.com/oturing/oopy/blob/master/exercicios/contador/contador.py

Instâncias da classe ``Contador`` servem para contar itens, por exemplo,
contar as ocorrências de determinadas palavras em um texto.

Veja podemos usar um contador para contar as vogais em uma palavra::

    >>> from contador import *
    >>> c = Contador()
    >>> for letra in 'abacaxi':
    ...     if letra in 'aeiou':
    ...         c.incrementar(letra)
    >>> c.contagem('a')
    3
    >>> c.contagem('i')
    1

Esta classe ``Contador`` tem o inconveniente de levantar uma exceção quando
pedimos a contagem de um item que não foi contado nenhuma vez::

    >>> c.contagem('u')
    Traceback (most recent call last):
      ...
    KeyError: 'u'

Antes de prosseguir para o Exercício 1.2, leia o código-fonte da classe
contador no módulo `contador.py` e entenda seu funcionamento.

Além disso, baixe os arquivos indicados em `Material necessário`_ para um
diretório local, e execute os testes, assim::

    $ python testar_doc.py contador.rst

O resultado será a exibição de uma falha, mais ou menos assim::

    **********************************************************************
    File "contador.rst", line 129, in contador.rst
    Failed example:
        ca = ContadorAmigavel()
    Exception raised:
        Traceback (most recent call last):
          File "/usr/local/lib/python2.7/doctest.py", line 1254, in __run
            compileflags, 1) in test.globs
          File "<doctest contador.rst[6]>", line 1, in <module>
            ca = ContadorAmigavel()
        NameError: name 'ContadorAmigavel' is not defined
    **********************************************************************
    1 items had failures:
      15 of  21 in contador.rst
    ***Test Failed*** 15 failures.
    ************************* ATENCAO: exibindo apenas o primeiro teste que falhou!

Esta falha indica precisamente qual é a sua próxima tarefa: implementar a
classe ``ContadorAmigavel``, conforme as instruções do Exercício 1.2.

Se você conseguiu rodar o teste e ver o erro ``NameError: name
'ContadorAmigavel' is not defined``, parabéns, você completou o Exercício 1.1!

Em caso de dúvidas, escreva para o `grupo de discussão Oficinas Turing`_.

Extra
-----

Leia a implementação do script ``testar_doc.py``. É um exemplo simples de uso
da API do módulo Doctest.

Exercício 1.2: o contador amigável
===================================

Sua primeira missão é desenvolver um contador mais tolerante, batizado de
``ContadorAmigo`` pela nossa equipe de marketing.

O ``ContadorAmigo`` tem um método ``contagem`` que devolve ``0`` quando um
item nunca foi contado::

    >>> ca = ContadorAmigavel()
    >>> for letra in 'abc':
    ...    ca.incrementar(letra)
    >>> ca.contagem('a')
    1
    >>> ca.contagem('z')
    0

Dica de implementação
---------------------

Implemente o ``ContadorAmigo`` como uma subclasse de ``Contador`` que apenas
sobrescreve o método ``contagem``.

Exercício 1.3: o contador totalizador
=====================================

O ``ContadorTotalizador`` mantém um atributo público ``total`` com a
quantidade de todos os itens contados. Implemente este contador como
subclasse direta da classe ``Contador`` (isso é importante em função
de um exercício posterior).

Exemplo de uso::

    >>> ct = ContadorTotalizador()
    >>> for letra in 'banana':
    ...    ct.incrementar(letra)
    >>> ct.total
    6

Dica de implementação
---------------------

Para inicializar o campo ``total`` na instância, você terá que sobrescrever o
método inicializador ("construtor"). Não se esqueça de invocar o inicializador
de ``Contador`` no inicializador de ``ContadorTotalizador``. Em geral, é uma
boa prática invocar o inicializador da superclasse antes de fazer qualquer
coisa no inicializdor da subclasse.

Também será necessário sobrescrever o método ``incrementar`` para atualizar
 o ``total``. Novamente, não esqueça de aproveitar o código do método
``Contador.incrementar``, invocando-o no início da sua implementação de
``incrementar``.

Exercício 1.4: melhorando o contador totalizador
================================================

O registro do total de itens permite implementar o método ``porcentagem`` que
devolve a proporção de cada item no total. O próximo passo é implementar este
método, que deverá devolver um ``float`` com a porcentagem::

    >>> ct.porcentagem('a') # considerando as letras de 'banana'
    50.0

Nos exemplos as seguir, arrendondamos os resultados para evitar variações na
representação de ``float`` em diferentes plataformas, conforme a dica na
`documentação do módulo Doctest`_.

::

    >>> round(ct.porcentagem('n'), 1)
    33.3
    >>> round(ct.porcentagem('b'), 1)
    16.7

.. _documentação do módulo Doctest: http://docs.python.org/library/doctest.html#warnings

Dica de implementação
---------------------

Este passo é mais simples que o anterior. O único cuidado especial, se você
estiver usando Python 2.x, é converter a contagem do item para ``float``, pois
tanto a contagem quanto o total serão ``int``, e divisão neste caso resultará
sempre em 0 (ou 1, se todos os itens contados forem iguais).

Extra
-----

Em sua implementação de ``porcentagem`` você invocou o método ``contagem``?
Justifique a sua decisão.

Exercício 1.5: o contador totalizador amigável
==============================================

Usando herança múltipla, implemente uma classe que combina as caracerísticas
do ``ContadorTotalizador`` e ``ContadorAmigavel``.

Ela deve funcionar assim::

    >>> cta = ContadorTotalizadorAmigavel()
    >>> for letra in 'laranja':
    ...    cta.incrementar(letra)
    >>> cta.total
    7
    >>> cta.contagem('a')
    3
    >>> cta.contagem('x')
    0
    >>> round(cta.porcentagem('a'), 1)
    42.9
    >>> round(cta.porcentagem('x'), 1)
    0.0

Extra
-----

Neste exercício, faz diferença a ordem das referências às superclasses na
declaração da classe ``ContadorTotalizadorAmigavel``? Justifique.
