# coding: utf-8

"""
Código inicial usado na Lista de Exercícios 1 do curso
"Objetos Pythonicos" de Luciano Ramalho, Oficinas Turing.
"""

class Contador(object):
    def __init__(self):
        self.totais = {}
        
    def contar(self, item):
        qtd = self.totais.get(item, 0) + 1
        self.totais[item] = qtd

    def contagem(self, item):
        return self.totais[item]
