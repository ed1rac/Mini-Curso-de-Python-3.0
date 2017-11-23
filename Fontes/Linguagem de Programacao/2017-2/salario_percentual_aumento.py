#entrada
salario = float(input('Digite o salário do funcionário: '))
percentual = float(input('Digite o percentual: '))

#processamento
aumento = salario * percentual / 100
novo_salario = salario + aumento

#saida
print('O salário é = ', salario, '.', ' O aumento = ', aumento)
print('O novo salário é: ', novo_salario)

