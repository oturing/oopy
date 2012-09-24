# coding: utf-8

from glob import glob
import os

IGNORAR = {'.' + ext for ext in
            ['pyc', 'class', 'rst']
        }

langs = {
    '.c':'c',
    '.py': 'python',
    '.java': 'java'}

for path_arq in glob('exemplos/*.*'):
    _, nome_arq = os.path.split(path_arq)
    nome, ext = os.path.splitext(nome_arq)
    if ext in IGNORAR:
        continue
    titulo = nome_arq
    print titulo
    print '-' * len(titulo)
    print
    print '.. literalinclude::', path_arq
    print '   :language:', langs[ext]
    print '   :linenos:'
    print '   :tab-width: 4'
    print

