def multiplica(num1, num2):
    if num1==0 or num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    else:
        return (num1 + multiplica(num1,num2 - 1))



resultado = multiplica(5,4)
print(resultado)
