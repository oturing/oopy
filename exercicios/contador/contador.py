# coding: utf-8

"""
Código inicial usado na Lista de Exercícios 1 do curso
"Objetos Pythonicos" de Luciano Ramalho, Oficinas Turing.
"""

class Contador(object):

    def __init__(self):
        self.ocorrencias = {}

    def incrementar(self, item):
        qtd = self.ocorrencias.get(item, 0) + 1
        self.ocorrencias[item] = qtd

    def contagem(self, item):
        return self.ocorrencias[item]

class ContadorAmigavel(Contador):

    def contagem(self, item):
        return self.ocorrencias.get(item, 0)

class ContadorTotalizador(Contador):

    def __init__(self):
        Contador.__init__(self)
        self.total = 0

    def incrementar(self, item):
        Contador.incrementar(self, item)
        self.total += 1

    def porcentagem(self, item):
        return float(self.contagem(item))/self.total*100

class ContadorTotalizadorAmigavel(ContadorTotalizador, ContadorAmigavel):
    '''devolve zero para itens inexistentes e calcula porcentagem'''




