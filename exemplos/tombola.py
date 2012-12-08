# coding: utf-8

class Tombola(object):
    '''sorteia itens'''

    def __init__(self):
        self.itens = []

    def carregar(self, itens):
        self.itens.extend(itens)

    def __contains__(self, el):
        return el in self.itens

    @property
    def carregada(self):
        return bool(self.itens)

    def misturar(self, embaralhadora):
        embaralhadora(self.itens)

