# coding=utf-8
def exibe_lista(lista):
    #for i in lista:
    print(lista)


def pesquisa_binaria(lista, item):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = int((primeiro + ultimo) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]
outra_lista = []

import random
random.seed()
for x in range(20):
    num = random.randint(1, 1000)
    outra_lista.append(num)

print (pesquisa_binaria(minha_lista, 3))
print (pesquisa_binaria(minha_lista, -1))
print ('lista gerada pelo computador:')
print ('Desordenada: ')
exibe_lista(outra_lista)
print ('')
print ('ordenada: ')
outra_lista.sort()
exibe_lista(outra_lista)
print (pesquisa_binaria(outra_lista, int(input("Digite um numero: "))))
