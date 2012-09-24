======================
Lista 2: Questão bônus
======================

Esta é uma questão avançada, não se sinta mal se não tiver tempo para
resolvê-la.

Considere uma mesma instância de tômbola iterável (como implementada no
exerício 2.2). Se tal tômbola for utilizada em dois laços ``for``, as
iterações serão independentes ou não?

Em termos práticos, sua implementação apresenta este comportamento::

    >>> t = Tombola()
    >>> t.carregar([1, 2, 3])
    >>> for i in t:
    ...    print i
    ...    break
    3
    >>> for i in t:
    ...    print i
    2
    1

Ou este outro comportamento? ::

    >>> t = Tombola()
    >>> t.carregar([1, 2, 3])
    >>> for i in t:
    ...    print i
    ...    break
    3
    >>> for i in t:
    ...    print i
    3
    2
    1
