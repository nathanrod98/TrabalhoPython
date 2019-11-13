#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


nome = []
notas = []
for i in range(0,10):
    nome = [(input('Digite o nome do aluno'))]
    for j in range(0,4):
        notas = [(float(input('Digite a nota')))]
a = 0

for aluno in nome:
    print(aluno)
    media = 0
    for i in range(a,a+4):
        media += notas[i]

     






        




