# coding: utf-8

"""
============================================================
Exemplo de uso de ``FrozenDate.today`` para facilitar testes
============================================================

O cálculo da idade de uma pessoa é por padrão relativo à data de hoje, mas
esta data varia. Para testar esse tipo de função, pode-se usar injeção de
dependência, fornecendo uma versão modificada do método ``today`` que devolver
sempre a mesma data.

O teste abaixo pode funcionar no dia em que ele foi escrito, mas como depende
da data atual ele vai parar de funcionar com o passar to tempo, por isso
fazemos ``+SKIP``::

    >>> nascimento = date(1963, 11, 12)
    >>> idade(nascimento) # doctest: +SKIP
    48

Para facilitar o teste, modificamos a função ``idade`` para aceitar como
argumento a função que será usada para determinar a data de hoje. Usando
``Frozendate.today``, "hoje" é sempre 8/set/2001::

    >>> from frozendate import FrozenDate
    >>> idade(nascimento, FrozenDate.today)
    37


"""

from datetime import date

def idade(nascimento, fn_hoje=date.today):
    hoje = fn_hoje()
    ja_fez = (nascimento.month, nascimento.day) <= (hoje.month, hoje.day)
    if ja_fez:
        return hoje.year - nascimento.year
    else:
        return hoje.year - nascimento.year - 1

