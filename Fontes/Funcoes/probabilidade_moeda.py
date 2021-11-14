# -*- coding: UTF-8 -*-
"""
Função:
    Exemplo de lançamento de moeda
Autor:
    Professor Ed - Data: 29/05/2016 -
Observações:  ?
"""
def gera_matriz_lancamentos(matriz, tamanho):
	import random
	matriz_faces = []
	print ('Gerando...')
	for x in range(tamanho):
		num = random.randint(1,2) #1 = cara, 2 = coroa
		matriz.append (num)
		
		if num==1:
			matriz_faces.append('Cara')
		else:
			matriz_faces.append('Coroa')

	print (matriz_faces)


def calcula_probabilidades(matriz, tamanho):
	soma_cara = 0
	soma_coroa = 0
	
	for i in range(len(matriz)):
		if matriz[i]==1:
			soma_cara = soma_cara+1
		elif matriz[i]==2:
			soma_coroa = soma_coroa + 1
	
	probabilidade_cara = float(soma_cara)/float(tamanho)*100
	probabilidade_coroa = float(soma_coroa)/float(tamanho)*100	
	
	print ('Foram lancadas ' + str(soma_cara) + ' caras e ' + str(soma_coroa) + ' coroas')

	probabilidades = []
	probabilidades.append(probabilidade_cara)
	probabilidades.append(probabilidade_coroa)	
	
	return probabilidades


matriz=[]
tamanho = int(input('Digite o tamanho da matriz de lancamentos: '))
gera_matriz_lancamentos(matriz, tamanho)
#print 'Um para cara e 2 para coroa'
#print matriz
vetor_probabilidades = []
vetor_probabilidades = calcula_probabilidades(matriz, tamanho)
print(f'As probabilidades sao: {vetor_probabilidades[0]} e {vetor_probabilidades[1]}')