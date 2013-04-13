# coding: utf-8

from abc import ABCMeta, abstractmethod

class Cao(object):
    __metaclass__ = ABCMeta

    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def latir(self, vezes=1):
        ''' exibe o latido (com print) '''

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao({0!r})'.format(self.nome)
