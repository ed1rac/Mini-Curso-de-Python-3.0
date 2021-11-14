lista = ['A', 'B', 'C']
print ('lista:', lista)

# A lista vazia é avaliada como falsa
while lista:
    # Em filas, o primeiro item é o primeiro a sair
    # pop(0) remove e retorna o primeiro item
    print ('Saiu', lista.pop(0), ', faltam', len(lista))

# Mais itens na lista
lista += ['D', 'E', 'F']
print ('lista:', lista)

while lista:
    # Em pilhas, o primeiro item é o último a sair
    # pop() remove e retorna o último item
    print ('Saiu', lista.pop(), ', faltam', len(lista))
