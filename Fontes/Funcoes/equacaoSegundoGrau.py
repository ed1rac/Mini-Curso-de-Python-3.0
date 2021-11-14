# coding=utf-8
"""
Funcao:
    Equação do segundo grau
Autor:
    Ed - Data: 20/05/2016 -
Observações: COmplexidade: ?
"""
#Com anotações
def eq2(a: int, b: int, c: int):
    """Retorna raízes para equações de 2º grau"""
    if a==0:
        return -c/b
    else:
        delta = (b**2 - 4*a*c)**0.5
        x1 = (-b - delta) / (2*a)
        x2 = (-b + delta) / (2*a)        
        return x1,x2

#testando a função
print(eq2(1,-5,6))
print(eq2(0,2,-2))
print(eq2(2,2,0))
print(eq2(2,0,2))
