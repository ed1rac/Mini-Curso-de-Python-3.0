# encoding: utf-8
""" 
Números perfeitos
Descrição:
    Esse algoritmo serve para verificar se um número é perfeito ou não.
    Números perfeitos são aqueles cuja soma dos divisores (exceto ele mesmo) é
    igual ao próprio número, como por exemplo 6, cujos divisores são 1, 2 e 3
    e 1+2+3 = 6
    Ele usa programação dinâmica
Complexidade:
      ?
Referências:
      http://en.wikipedia.org/wiki/Perfect_numbers
"""

def calc_perf(number):
  contador = 1
  divisores = []
  soma = 0
  while contador <= number/2:
    if number%contador == 0:
      divisores.append(contador)
    contador += 1
  for divisor in divisores:
    temp = divisor
    soma += divisor
  if soma == number:
    #print ("This is a perfect number")
    print("\nDivisores: ",divisores, "\nSoma: ", soma)  
    return True
  else:
    #print ("This is not a perfect number try again")
    return False

if(calc_perf(8128)):
    print("O numero 8128 é perfeito")

print("Calculando perfeitos")
for i in range(1,10000):
    if(calc_perf(i)):
        print("O numero",i," é perfeito")
