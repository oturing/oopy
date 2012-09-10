# coding: utf-8

"""
Classe Cão

    >>> rex = Cao('Rex')
    >>> rex
    Cao('Rex')
    >>> print rex
    Rex
    >>> rex.qt_patas
    4
    >>> rex.latir()
    Rex: Au!
    >>> rex.latir(2)
    Rex: Au! Au!
    >>> rex.nervoso = True
    >>> rex.latir(3)
    Rex: Au! Au! Au! Au! Au! Au!
"""

class Mamifero(object):
    """lição de casa: implementar"""

class Cao(Mamifero):
    qt_patas = 4
    carnivoro = True
    nervoso = False
    def __init__(self, nome):
        self.nome = nome
    def latir(self, vezes=1):
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print self.nome + ':' + ' Au!' * vezes
    def __str__(self):
        return self.nome
    def __repr__(self):
        return 'Cao({0!r})'.format(self.nome)
        
class Pequines(Cao):
    """ O pequinês está normalmente nervoso:
    
         >>> fido = Pequines('Fido')
         >>> fido.latir()
         Fido: Au! Au!
    """
    nervoso = True
    
class Mastiff(Cao):
    """ O mastiff late diferente:
    
         >>> atos = Mastiff('Atos')
         >>> atos.latir()
         Atos: Wuff!
    """
    def latir(self, vezes=1):
        # o mastiff não muda seu latido quando nervoso
        print self.nome + ':' + ' Wuff!' * vezes
        
class SaoBernardo(Cao):
    """O São Bernardo serve conhaque:
    
        >>> sansao = SaoBernardo('Sansao')
        >>> sansao.servir()
        Sansao serve o conhaque (restam 9 doses)
        >>> sansao.doses = 1
        >>> sansao.servir()
        Sansao serve o conhaque (restam 0 doses)
        >>> sansao.servir()
        Traceback (most recent call last):
          ...
        ValueError: Acabou o conhaque!
    """
    def __init__(self, nome):
        Cao.__init__(self, nome)
        self.doses = 10
    def servir(self):
        if self.doses == 0:
            raise ValueError('Acabou o conhaque!')
        self.doses -= 1
        msg = '{0} serve o conhaque (restam {1} doses)'
        print msg.format(self.nome, self.doses)
