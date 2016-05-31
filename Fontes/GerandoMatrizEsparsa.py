# Matriz em forma de string
matriz = '''0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0
0 0 0 0 6 0 0 0 0 0 0 0'''

mat = {}

# Quebra a matriz em linhas
for lin, linha in enumerate(matriz.splitlines()):

    # Quebra a linha em colunas
    for col, coluna in enumerate(linha.split()):

        coluna = int(coluna)
        # Coloca a coluna no resultado,
        # se for diferente de zero
        if coluna:
            mat[lin, col] = coluna

print (mat)
# Some um nas dimensões pois a contagem começa em zero
print ('Tamanho da matriz completa:', (lin + 1) * (col + 1))
print ('Tamanho da matriz esparsa:', len(mat))
