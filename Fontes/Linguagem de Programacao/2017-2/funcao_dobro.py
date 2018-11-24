"""
" Função que calcula o dobro de um numero
"
"""
def dobro(num):
    return 2 * num


print('Programa que calcula o dobro de um número')
numero = float(input('Digite um número: '))
db = dobro(numero)
print('O dobro de ', numero, ' é ', db)
