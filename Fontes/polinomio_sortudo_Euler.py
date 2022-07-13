def lucky(k):
	return k * k - k + 41

lista = []

for x in range(1,50):
	print("Lucky number\(", x, ") = ", lucky(x))
	lista.append(lucky(x))


print(lista)
