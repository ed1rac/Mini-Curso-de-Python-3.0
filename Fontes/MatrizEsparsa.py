# Matriz esparsa implementada
# com dicionário

# Matriz esparsa é uma estrutura
# que só armazena os valores que
# existem na matriz

dim = 6, 12
mat = {}

# Tuplas são imutáveis
# Cada tupla representa
# uma posição na matriz
mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9

for lin in range(dim[0]):
    for col in range(dim[1]):
        # Método get(chave, valor)
        # retorna o valor da chave
        # no dicionário ou se a chave
        # não existir, retorna o
        # segundo argumento
        print (mat.get((lin, col), 0),end=' ')
    print()
