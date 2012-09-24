# coding: utf-8

'''
Manipulação *in-place* (no local) de sequências mutáveis, para
simular ``random.shuffle`` que é difícil de testar.
'''

def pairswap(seq):
    '''Inverte a posição dos sucessivos pares de itens

        >>> l = [1, 2, 3, 4]
        >>> pairswap(l)
        >>> l
        [2, 1, 4, 3]
        >>> l = [1, 2, 3]
        >>> pairswap(l)
        >>> l
        [2, 1, 3]
        >>> l = [1]
        >>> pairswap(l)
        >>> l
        [1]
        >>> l = []
        >>> pairswap(l)
        >>> l
        []

    '''
    for i in range(0, len(seq)-1, 2):
        seq[i], seq[i+1] = seq[i+1], seq[i]

