# coding: utf-8

from carta_ord import Carta

class Baralho(object):

    def __init__(self):
        self.cartas = Carta.todas()

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, pos, valor):
        self.cartas[pos] = valor




