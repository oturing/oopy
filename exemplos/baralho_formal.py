from collections import MutableSequence

class Carta(object):
    naipes = 'paus copas espadas ouros'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

    @classmethod
    def todas(cls):
        return [cls(v, n) for n in cls.naipes
                          for v in cls.valores] 

class Baralho(MutableSequence):
    def __init__(self):
        self.cartas = Cartas.todas()
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
