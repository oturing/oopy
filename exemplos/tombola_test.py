# coding: utf-8

import unittest

from tombola import Tombola

class TestarUsosBasicos(unittest.TestCase):

    def setUp(self):
        self.tombola = Tombola()

    def testar_carregada(self):
        self.assertFalse(self.tombola.carregada())

    def testar_carregar_e_carregada(self):
        self.tombola.carregar('ABC')
        self.assertTrue(self.tombola.carregada())

    def testar_sortear(self):
        itens = [1]
        self.tombola.carregar(itens)
        res = self.tombola.sortear()
        self.assertEqual(res, itens[0])

if __name__ == '__main__':
    unittest.main()
