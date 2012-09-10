# coding: utf-8

'''
ATENÇÃO: Esta implementação da classe contador tem um bug sério 
relacionado ao compartilhamento de um objeto mutável. A finalidade
deste código é servir de ponto de partida para um exercício
'''

class Contador(object):
    contagem = {}
        
    def incluir(self, item):
        qtd = self.contagem.get(item, 0) + 1
        self.contagem[item] = qtd

    def contar(self, item):
        return self.contagem[item]
        