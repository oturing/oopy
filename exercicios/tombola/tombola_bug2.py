# coding: utf-8

"""
===========================
Testando um tômbola com bug
===========================

Para começar, vamos criar uma instância de tômbola. Nessa implementação,
é opcional fornecer uma sequência de itens ao construtor::

    >>> t1 = Tombola()
    >>> t1.carregada()
    False

Em seguida vamos carregar a tômbola::

    >>> t1.carregar([11, 22, 33])
    >>> t1.carregada()
    True

Agora vamos revelar o bug, criando uma nova tômbola::

    >>> t2 = Tombola()
    >>> t2.carregada()
    True

A nova tômbola já aparece carregada! Quais são seus itens?

    >>> t2.itens
    [11, 22, 33]
    >>> t2.itens is t1.itens
    True

Note que objeto ``t2.itens`` é *o mesmo* que ``t1.itens`` (não apenas igual).

Isso acontece porque o valor default do parâmetro ``seq=[]`` é armazenado no
objeto função ``__init__``. Quando não é passado um argumento ``seq`` a
atribuição ``self.itens = seq`` cria um *alias* (um apelido) para o valor
default.

Isso não seria um problema se o valor fosse imutável. Mas ele é mutável
e no método ``carregar`` ele é modificado pelo método ``extend``.

Portanto quando carregamos a tômbola ``t1`` na verdade estamos modificando
o valor default do parâmetro ``seq=[]``! Podemos provar isso acessando o
atributo ``func_defaults`` de ``__init__``, que contém os valores default
dos parâmetros da função, armazenados em uma tupla::

    >>> Tombola.__init__.func_defaults
    ([11, 22, 33],)
    >>> Tombola.__init__.func_defaults[0] is t1.itens
    True
    >>> Tombola.__init__.func_defaults[0] is t2.itens
    True
    >>>

Observe que a lista em ``func_defaults[0]`` é exatamente o mesmo objeto
referenciado por ``t1.itens`` e ``t2.itens``.

Por este motivo é considerado uma prática arriscada usar objetos mutáveis
como valores default para parâmetros de função. Uma implementação melhor para
o ``__init__`` seria::

    def __init__(self, seq=None):
        if seq is None:
            self.itens = []
        else:
            self.itens = seq

Ou a mesma coisa em uma linha usando o operador ternário::

    def __init__(self, seq=None):
        self.itens = [] if seq is None else seq

Uma outra medida que pode ser interessante quando se manipula um argumento
mutável (como ``seq`` neste exemplo) é criar uma cópia dele, para evitar
efeitos colaterais indesejáveis. Veja o exemplo ``tombola_bug.py`` neste
diretório para uma discussão sobre esta questão relacionada.

"""

class Tombola(object):
    '''IMPLEMENTACAO COM BUG!!!'''

    def __init__(self, seq=[]):
        self.itens = seq

    def carregar(self, seq):
        self.itens.extend(seq)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)
