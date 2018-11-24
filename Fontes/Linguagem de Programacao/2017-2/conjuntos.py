linguagens = ["Python", "Java", "C#", "PHP"]
print("Eu gosto de " + linguagens[0])
print("A linguagem que eu menos gosto é " + linguagens[-1])

lista_aninhada = [[1, 2, 3], [10, 20, 30]]
print(lista_aninhada[0][1])
print(lista_aninhada[1][2])

lista_com_diferentes_tipos = ["TreinaWeb", 10, True]
print(lista_com_diferentes_tipos[0])
print(lista_com_diferentes_tipos[1])
print(lista_com_diferentes_tipos[2])

exemplo_tupla = ("Isso", "é", "uma", "tupla")
print(exemplo_tupla[0])
#exemplo_tupla[0] = "Mudei"
print(exemplo_tupla[0])

exemplo_slice = linguagens[1:3]
print(exemplo_slice)
outro_slice = linguagens[:2]
print(outro_slice)
mais_um_slice = linguagens[1:]
print(mais_um_slice)

print(len(linguagens))
print(len(exemplo_tupla))
print(len(exemplo_slice))

print("Python" in linguagens)
print("Perl" in linguagens)

print(linguagens * 3)

linguagens.append("Perl")
linguagens.append("OCaml")
print(linguagens)

linguagens.extend(["JavaScript", "C", "C++"])
linguagens.extend(("IronPython", "Ruby"))
print(linguagens)

linguagens += "R"
linguagens += ("Clipper", "Elixir")
print(linguagens)

primeira_linguagem = linguagens.pop(0)
print(primeira_linguagem)
print(linguagens)
ultima_linguagem = linguagens.pop()
print(ultima_linguagem)
print(linguagens)

linguagens.remove("R")
print(linguagens)
#linguagens.remove("Python")

indice_C = linguagens.index("C")
print(indice_C)
#outro_indice_C = linguagens.index("C", 1, 4)
#print(outro_indice_C)
outro_indice_C = linguagens.index("C", 1)
print(outro_indice_C)

linguagens.insert(0, "Python")
print(linguagens)
linguagens.insert(4, "Rust")
print(linguagens)
linguagens.insert(1000, "VB.NET")
print(linguagens)