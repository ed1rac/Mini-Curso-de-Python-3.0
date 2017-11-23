num = int(input('Digite um número: '))
i = 1
quant = 0
while(quant<20):
    if(i%num==0):
        print(i)
        quant+=1
    i+=1
