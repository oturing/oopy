#!/usr/bin/env python 

import sys
import doctest

def main():
    if len(sys.argv) != 2:
        print('modo de usar: {0} arquivo.rst'.format(sys.argv[0]))
        return 2
    else:
        nome_doc = sys.argv[1]
        qt_falhas, qt_testes = doctest.testfile(nome_doc, 
                                module_relative=False, 
                                optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
        if qt_falhas:
            print ' ATENCAO: exibindo apenas o primeiro teste que falhou!'.rjust(79, '*')
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())