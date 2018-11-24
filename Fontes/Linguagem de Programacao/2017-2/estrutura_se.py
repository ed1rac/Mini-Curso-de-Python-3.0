idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")
    print("outra coisa")
else:
    print("Você é menor de idade.")
if idade < 18:
    print("Você é criança")
elif idade >= 18 and idade <= 65:
    print("Você é adulto")
else:
    print("Você é idoso")