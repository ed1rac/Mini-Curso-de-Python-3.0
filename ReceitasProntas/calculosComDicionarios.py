#
# Problema - Fazendo cálculos com dicionários
# Autor: Ed - Data: 20/05/2015
# Observacoes: PC - PB 1.8 - P. 32
# 
precos={
	'MSFT': 45.23,
	'APPL': 612.78,
	'IBM': 205.54,
	'HPQ': 37.20,
	'FB': 12.15
	}
# Para executar calculos uteis com o conteudo do dicionario
# , em geral, é útil inverter as chaves e os valores do dicionário
# utilizando zip() conforme exemplo abaixo
print("O original é: \n", precos)
precoMinimo = min(zip(precos.values(), precos.keys()))
print('O preço mínimo é: ', precoMinimo)
print('chaves invertidas: ', precos)
precoMaximo = max(zip(precos.values(), precos.keys()))
print('O preço máximo é: ', precoMaximo)
precosOrdenado = sorted(zip(precos.values(), precos.keys()))
print("Ordenados: \n", precosOrdenado)
# Lembrando que zip() gera um iterador que pode ser consumido
# somente uma vez
#==========================================================
#Extraindo um subconjunto de um dicionario
p1={key:value for key, value in precos.items() if value > 200}
print("As acoes acima de 200 sao: \n" , p1)
#==========================================================
#Somando os elementos dicionario
soma = sum(x for x in precos.values())
print('A soma dos valores de todas as acoes = ', soma)
