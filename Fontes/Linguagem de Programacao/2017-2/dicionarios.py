nomes = { "João" : "da Silva", "Maria" : "Souza", "José" : "dos Reis" }
print(nomes)

print("João " + nomes["João"])
#print("Pedro " + nomes["Pedro"])

print(len(nomes))

print("João" in nomes)
print("Pedro" in nomes)

del nomes["João"]
print(nomes)


nomes["TreinaWeb"] = "Cursos"
print(nomes)

sobrenome = nomes.pop("TreinaWeb")
print(sobrenome)
print(nomes)


mais_nomes = { "TreinaWeb" : "Cursos", "Pedro" : "de Lara"}
nomes.update(mais_nomes)
print(nomes)