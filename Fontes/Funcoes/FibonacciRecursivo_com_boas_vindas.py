def fib(n):
  """
  Fibonacci:
  fib(n) = fib(n-1) + fib(n-2), se n> 1
  fib(n) = 1, se n >= 1
  """
  if n > 1:
    return fib(n-1)+fib(n-2)
  else:
    return 1

def pedir_numero():
  numero = int(input('Digite um numero inteiro: '))
  return numero

def tela_boas_vindas(nome_programa):
  print("*****************************************************")
  print("     Bem vindo ao programa:", nome_programa)
  print("*****************************************************")

#testando a função
tela_boas_vindas('Fibonacci recursivo')
num = pedir_numero()
for i in range(0, num+1):
  print('Fib(',i, ') => ', fib(i))