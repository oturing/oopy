from collections import MutableSequence

from carta_ord import Carta

class Baralho(MutableSequence):

    def __init__(self):
        self.cartas = Carta.todas()

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, pos, valor):
        self.cartas[pos] = valor

    def __delitem__(self, pos):
        del self.cartas[pos]

    def insert(self, pos, valor):
        self.cartas.insert(pos, valor)
