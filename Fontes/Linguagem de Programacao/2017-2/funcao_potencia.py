"""
" Função que calcula x elevado a y
" Autor: gainho Ed
" Data: algum dia de algum mes de algum ano
"
"""
def potencia(x, y):
    return x ** y

def pula(x):
    for i in range(x):
        print('')

print('Programa que calcula x elevado a y')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
pot = potencia(num1, num2)
pula(2)
print(num1, ' ^ ', num2, ' = ', pot)

