def somatorio(num):
    soma = 0 #variável ACUMULADORA
    for i in range(num+1):
        soma+=i #soma <- soma + i

    return soma

print(somatorio(5)) 