# coding: utf-8

import random

class Tombola(object):
    def __init__(self):
        self.itens = []

    def carregar(self, itens):
        self.itens = list(itens)

    def carregada(self):
        return bool(self.itens)

    def misturar(self):
        random.shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()
