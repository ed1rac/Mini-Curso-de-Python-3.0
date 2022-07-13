#
# Metodo ZIP()
#
primeiro = [1,3,5,7,9]
segundo = [2,4,6,8,10]

for x,y in zip(primeiro, segundo):
    print(x + y)

# # # # # # # # # # # # # # # #
#
# Metodo MAP()
#
def raiz(x):
    return x**0.5
# Jeito classico
raizes = []
nums = [4,9,27,32,78,98,45,22]
for num in nums:
    raizes.append(raiz(num))

# Forma com map()
raizes =[]
raizes = map(raiz, nums)
print(raizes)
