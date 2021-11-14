dados = [(4, 3), (5, 1), (7, 2), (9, 0)]

# Comparando pelo último elemento
def _cmp(x, y):
    return cmp(x[-1], y[-1])

print ('Lista:', dados)

# Ordena usando _cmp()
print ('Ordenada:', sorted(dados, _cmp))


