# coding: utf-8

"""
=====================================
Subclasse fajuta de ``datetime.date``
=====================================

A classe ``FrozenDate`` sobrescreve o método ``date.today`` para devolver
sempre uma determinada data: 8 de setembro de 2001, o dia em que os segundos
transcorridos da época UNIX chegaram a 1.000.000.

    >>> d = FrozenDate.today()
    >>> d
    datetime.date(2001, 9, 8)

"""

from datetime import date

class FrozenDate(date):

    @staticmethod
    def today():
        return date.fromtimestamp(10**9) # 2001-09-08

# Curiosidade:
# se existe o método date.fromtimestamp, porque não existe date.totimestamp?
# resposta do Tim Peters aqui:
#
# http://bytes.com/topic/python/answers/522572-datetime-timestamp
#
#  Because datetime objects have greater range and precision than timestamps,
#  conversion is problem-free in only one direction. It's not a coincidence
#  that that's the only direction datetime supplies ;-)
