"""
Programa para ver a nota de um aluno baseado em quantos programas/questões
ele fez
Autor: Ed - Data: 20/05/2016 - Observações
"""
totalQuestoes = 26 #Trabalho - Pratica Java
questoesFeitas = int(input("Digite a quantidade de questões resolvidas: "))
questoesErradas = int(input("Digite a quantidade de questões erradas: "))
nota = (questoesFeitas-questoesErradas)/totalQuestoes
print("\nQuestões = %d\nFeitas = %d" % (totalQuestoes,questoesFeitas))
print("Erradas = %d\nA nota = %f " % (questoesErradas,nota))
input()

