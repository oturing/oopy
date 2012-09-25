#!/usr/bin/env python
# coding: utf-8

'''
----------------------------------------------
Introdução ao doctest com exemplos e dicas 
----------------------------------------------

Um doctest é um teste automatizado embutido em uma docstring. Para executar 
doctests, usa-se a função `doctest.testmod()`, como no final deste arquivo. 

A função executa todas as linhas de entrada de código marcadas com o sinal
`>>>` e verifica se a saída é o que aparece na linha seguinte::

    >>> 2 + 3
    5
    >>> 2 ** 64
    18446744073709551616L

A sintaxe do doctest imita exatamente o que aparece no console interativo 
do Python:: 

    >>> 'bla' * 3
    'blablabla'
    >>> print 'bla' * 3
    blablabla

O doctest é rigoroso na checagem. Note que nos exemplos acima a primeira 
saída aparece entre aspas, e no segunda o resultado está sem aspas,
precisamente como vemos no console interativo.

Operações sem resultado
-----------------------

Quando uma operação não devolve um resultado, ou devolve `None`, nada aparece
na saída. Por exemplo, uma atribuição não devolve resultado, então é preciso
acessar a variável para verificar seu valor::

    >>> a = 2**10
    >>> a
    1024

O método `list.sort()` também não devolve um resultado, porque ele age sobre
a própria lista::

    >>> l = [2, 3, 1]
    >>> l.sort()
    >>> l
    [1, 2, 3]
    
Espaços
-------

Atenção para os espaços. Entre o sinal `>>>` e o código é preciso ter um
espaço, e apenas um.

Além disso, ao escrever listas e tuplas em Python, não faz diferença se 
existem ou não espaços antes ou depois colchetes, parênteses e vírgula. 
Mas ao conferir o doctest, Python espera encontrar um espaço somente após
cada vírgula::

    >>> range(7)
    [0, 1, 2, 3, 4, 5, 6]
    
      
Aspas
-----

Embora em Python você possa usar aspas simples ou duplas como preferir, o 
doctest espera sempre aspas simples na saída, porque é a assim que aparece
no console interativo::

    >>> "ca" + "sa"
    'casa'

Uma exceção é quando a string contem aspas simples::

    >>> 'bo' + "b's"
    "bob's"
    

Endentação
----------

Costuma-se endentar os exemplos de código, inclusive o sinal `>>>`, como
neste arquivo. Esta endentação, junto com o uso de dois pontos em dobro, 
serve para que o sistema de documentação do Python (docutils) coloque uma 
fonte especial para código nos exemplos, quando geramos HTML ou Latex.

Caso o código contenha blocos, use os mesmos marcadores de continuação 
(...) que funcionam no console interativo, e endente as linhas dentro 
do bloco::

    >>> for letra in 'caos':
    ...     print letra
    c
    a
    o
    s
        
Exceções
--------

Para testar exceções, basta colocar o cabeçalho e o detalhe da exceção::

    >>> float('boi')
    Traceback (most recent call last):
        ...
    ValueError: invalid literal for float(): boi
    
O cabeçalho é a linha que diz `Traceback...` e o detalhe começa com o nome 
da exceção: `ValueError:` no exemplo acima.

Qualquer texto entre o cabeçalho e o detalhe é ignorado no doctest. É 
convencional usar `...` neste caso, mas não é obrigatório.
    
Diretiva +SKIP: Pular um teste
------------------------------    
    
Se você não quer executar um determinado teste, pode desligá-lo com um 
comentário especial, usando a sintaxe `doctest: +SKIP`::

    >>> 7/0  # doctest: +SKIP
    (este teste não será executado)

Diretiva +ELLIPSIS: Ignorar valores incertos ou irrelevantes
------------------------------------------------------------
 
Às vezes não temos como saber tudo o que vai aparecer na saída do teste,
então podemos usar a diretiva `+ELLIPSIS` e colocar `...` no trecho que 
queremos ignorar. 

Por exemplo, posições de memória são impossíveis de prever, então neste
código ignoramos o número hexadecimal que apareceria depois do `0x`::

    >>> from random import random
    >>> random # doctest: +ELLIPSIS
    <built-in method random of Random object at 0x...>

O mesmo acontece com números aleatórios::

    >>> random() # doctest: +ELLIPSIS
    0...

Operações com ponto-flutuante também podem variar conforme o processador, 
mas nesse caso as primeiras casas decimais podem ser conferidas::

    >>> 12345 / 1000.0 # doctest: +ELLIPSIS
    12.34...

Os três pontos podem ser usados também para ignorar uma parte de um resultado
muito extenso::

    >>> range(1000) # doctest: +ELLIPSIS
    [0, 1, 2, ..., 998, 999]

Note que todos estes testes falhariam se não fosse usada a opção `+ELLIPSIS`.


Diretivas na chamada de `testmod()`
-----------------------------------

Observe que no final deste arquivo estão sendo usadas duas diretivas globais, 
para ter efeito sobre todos os testes::

- `REPORT_ONLY_FIRST_FAILURE`: para exibir só a primeira falha que ocorrer

- `NORMALIZE_WHITESPACE`: para ser tolerante com espaços no final das linhas

O operador `|` é usado para fazer a conjunção bit a bit destas opções, pois 
o argumento `optionflags` espera uma máscara de bits (bitmask).

Como executar os testes
-----------------------

Quando o código para executar a função `doctest.testmod()` está embutido 
no arquivo-fonte, basta executar o arquivo-fonte como um script na linha de 
comando. 

Por exemplo, para executar os testes deste arquivo no GNU/Linux::

    $ python intro_doctest.py
    
Ou, se o arquivo estiver assinalado como executável::

    $ ./intro_doctest.py
    
E no Windows::

    C:> intro_doctest.py    

Se todos os testes passarem, nada será exibido na saída. Para verificar quais
testes estão sendo executados, coloque a opção `-v` na linha de comando::

    $ python intro_doctest.py -v
    
Com a opção `-v` serão exibidos os testes, e ao final um relatório mais ou 
menos assim::

    1 items passed all tests:
      19 tests in __main__
    19 tests in 1 items.
    19 passed and 0 failed.
    Test passed.

Em caso de falhas, as diferenças entre os resultados esperados e obtidos
serão exibidas, e a última linha do relatório trará uma indicação assim::

    ***Test Failed*** 3 failures.
    
Na prática, evite rodar os testes a toda hora usando a opção `-v`, pois ela 
produz muito texto na saída e pode tornar difícil distinguir testes bem 
sucedidos de testes com falhas. Use o `-v` apenas para checar se os testes 
estão mesmo sendo executados, depois habitue-se a não usar esta opção.

'''

if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags=opcoes)

