# Progs e seus albuns
progs = {'Yes': ['Close To The Edge', 'Fragile'],
    'Genesis': ['Foxtrot', 'The Nursery Crime'],
    'ELP': ['Brain Salad Surgery']}

# Mais progs
progs['King Crimson'] = ['Red', 'Discipline']

# items() retorna uma lista de
# tuplas com a chave e o valor
for prog, albuns in progs.items():
    print (prog, '=>', albuns)
print(len(progs), 'bandas')

# Se tiver 'ELP', deleta
if 'ELP' in progs:
    del progs['ELP']

print('Agora', len(progs), 'bandas')
