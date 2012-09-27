# coding: utf-8

from abc import ABCMeta, abstractmethod, abstractproperty

class TombolaABC(object):
    '''Sorteia itens sem repetir'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def carregar(self, seq):
        '''coloca os itens de uma sequencia na tômbola'''

    @abstractmethod
    def sortear(self):
        '''devolve um item sorteado'''

    @abstractproperty
    def carregada(self):
        '''devolve `True` se há pelo menos um item a sortear'''

