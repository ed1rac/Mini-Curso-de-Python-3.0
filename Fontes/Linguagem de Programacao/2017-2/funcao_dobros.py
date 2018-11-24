"""
" Função que calcula o dobro de dois números
"
"""
def dobro(num):
    return 2 * num

def dobros(num1, num2):
    print('O dobro de ', num1, ' é ', dobro(num1))
    print('O dobro de ', num2, ' é ', dobro(num2))


print('Programa que calcula o dobro de dois números')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
dobros(numero1, numero2)

