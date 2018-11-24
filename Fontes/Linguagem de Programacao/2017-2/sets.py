set_treinaweb = set("TreinaWeb Cursos")
print(set_treinaweb)

set_treinaweb.add("e")
print(set_treinaweb)

set_linguagens = set(["Python", "C#", "Java"])
print(set_linguagens)
set_linguagens.add("Lisp")
print(set_linguagens)

set_congelado = frozenset(["Isso", "é", "um", "frozenset"])
print(set_congelado)

set_outras_linguagens = { "JavaScript", "C++", "Python" }
print(set_outras_linguagens)

set_diferencas_1 = set_linguagens.difference(set_outras_linguagens)
print(set_diferencas_1)
set_diferencas_2 = set_linguagens - set_outras_linguagens
print(set_diferencas_2)

set_outras_linguagens.discard("C++")
print(set_outras_linguagens)
set_outras_linguagens.discard("C")
print(set_outras_linguagens)

set_outras_linguagens.add("C")
print(set_outras_linguagens)
set_outras_linguagens.remove("C")
print(set_outras_linguagens)
#set_outras_linguagens.remove("C")

print(set_linguagens.union(set_outras_linguagens))
print(set_linguagens | set_outras_linguagens)

print(set_linguagens.intersection(set_outras_linguagens))
print(set_linguagens & set_outras_linguagens)

print(set_linguagens.isdisjoint(set_outras_linguagens))

set_linguagens.difference_update(set_outras_linguagens)
print(set_linguagens)