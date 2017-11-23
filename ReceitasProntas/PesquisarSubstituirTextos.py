#
# Problema - Pesquisar e substituir textos
# Autor: Ed - Data: 20/05/2015
# Observacoes: PyCk - PB 2.5 - p65
# 
linha = 'Edkallenn Silva de Lima; Casado; Professor, Servidor Público Federal,    Ed'
print("A linha é: \n", linha)
import re
linha2= linha.replace('Ed', 'De')
print("A linha2 é: \n", linha2)
#Para padroes complicados o ideal e' usar as funcoes/metodos sub()do modulo re
#Exemplo trocando as datas no formato 27/11/2015 para 2015-11-27
texto = "Hoje é 27/11/2015. O Evento é dia 13/03/2016"
print("O texto original é: \n", texto)
print("O texto alterado pela Expressao Regular é:")
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))
print('Rodou')
