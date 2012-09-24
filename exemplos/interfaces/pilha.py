# coding: utf-8

class PilhaSimples(object):
    def __init__(self):
        self.__itens = []
    def colocar(self, item):
        self.__itens.append(item)
    def retirar(self):
        if self.__itens:
            return self.__itens.pop()
        else:
            raise LookupError('pilha vazia')

