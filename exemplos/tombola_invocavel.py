# coding: utf-8

"""
-----------------
Tômbola invocável
-----------------

    >>> t = TombolaInvocavel()
    >>> t.carregar([99])
    >>> t()
    99

"""

from tombola import Tombola

class TombolaInvocavel(Tombola):
    '''Sorteia itens sem repetir; instância é invocável como uma função'''

    def __call__(self):
        return self.sortear()

