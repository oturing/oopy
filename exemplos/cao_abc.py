# coding: utf-8

from abc import ABCMeta, abstractmethod

class Cao(object):
    __metaclass__ = ABCMeta

    qt_patas = 4
    carnivoro = True

    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def latir(self, vezes=1):
        """ deve exibir o latido no stdout """

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao({0!r})'.format(self.nome)


class Viralata(Cao):
    """ Um cão genérico """

class Pequines(Cao):
    """ O pequinês está normalmente nervoso:

         >>> fido = Pequines('Fido')
         >>> fido.latir()
         Fido: Au! Au!
    """
    nervoso = True

    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print self.nome + ':' + ' Au!' * vezes


class Mastiff(Cao):
    """ O mastiff late diferente:

         >>> atos = Mastiff('Atos')
         >>> atos.latir()
         Atos: Wuff!
    """
    def latir(self, vezes=1):
        # o mastiff não muda seu latido quando nervoso
        print self.nome + ':' + ' Wuff!' * vezes
