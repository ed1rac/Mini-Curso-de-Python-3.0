"""
Função:
    Algumas funções estatísticas
Autor:
    Ed - Data: 20/05/2016 -
Observações: Complexidade: 1 ?
"""
#Com anotações
def media(lista):
    """retorna a media de uma quantidade n de argumentos"""
    return float(sum(lista)) / len(lista)


def mediana(lista):
    """retorna a mediana de uma lista de argumentos"""
    tamanho=len(lista)
    if tamanho%2==0:
        meio = int(tamanho/2)
        return (lista[meio-1]+lista[meio])/2
    else:
        return lista[int(tamanho/2)]

#testando a função
l = [23, 54, 31, 77, 12, 34]
print(l)
print('Média: ', media(l))
print('Mediana: ',mediana(l))
print('Acrescentando o elemento 13')
l.append(13)
print(l)
print('Média: ', media(l))
print('Mediana: ',mediana(l))
