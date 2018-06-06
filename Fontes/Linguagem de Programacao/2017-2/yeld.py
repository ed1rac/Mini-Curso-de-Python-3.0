# -*- coding: utf-8 -*-

def gerador():
        for i in range(10):
                yield i * 2


gera = gerador()
print(gera)
