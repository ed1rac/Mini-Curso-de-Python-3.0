#
# Problema - Separar Strings de acordo com vários delimitadores
# Autor: Ed - Data: 20/05/2015
# Observacoes: PytCbk - PB 2.1 - P. 56
# 
linha = 'Edkallenn Silva de Lima; Casado; Professor, Servidor Público Federal,    Ed'
print("A linha é: \n", linha)
import re
split = re.split(r'[;,\s]\s*', linha)
print("E depois de separada: \n", split)

