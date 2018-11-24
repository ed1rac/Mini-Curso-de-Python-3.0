# coding=utf-8
def somar(n1, n2):
    """Realiza a somatória de dois números"""
    print("{n1} + {n2} = {resultado}".format(n1=n1, n2=n2, resultado=n1+n2))


def subtrair(n1, n2):
    """Realiza a subtração de dois números"""
    return n1 - n2


def multiplicar(n1, n2):
    """Realiza a multiplicação de dois números"""
    return n1 * n2


def dividir(n1, n2):
    """Realiza a divisão de dois números, retornando o quociente e o resto"""
    return (n1 // n2, n1 % n2)


def media_aritmetica(*numeros):
    """Calcula a média aritmética dos números informados"""
    return sum(numeros) / len(numeros)


numero1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação: ")
numero2 = int(input("Digite o segundo número: "))
if operacao == "+":
    somar(numero1, numero2)
    print(somar.__doc__)
elif operacao == "-":
    resultado = subtrair(numero1, numero2)
    print("{n1} - {n2} = {resultado}".format(n1=numero1, n2=numero2, resultado=resultado))
elif operacao == "x":
    print("{n1} x {n2} = {resultado}".format(n1=numero1, n2=numero2, resultado=multiplicar(numero1, numero2)))
elif operacao == "/":
    quociente, resto = dividir(numero1, numero2)
    print("O quociente é ", quociente, " e o resto é ", resto)

print("Média artimética = {m}".format(m=media_aritmetica(3, 4, 5, 6)))
numeros = [10, 20, 30, 50, 60]
print("Outra média aritmética = {m}".format(m=media_aritmetica(*numeros)))