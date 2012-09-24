from random import shuffle

class Tombola(object):
    '''Sorteia itens sem repetir'''

    def carregar(self, seq):
        self.itens = list(seq)

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)
