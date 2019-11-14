#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


nome = []
notas = []
media = 0
a=0
b=1
c=2
d=3

for i in range(0,10):
    nome.append(input(f'Digite o nome do aluno: '))
    for j in range(0,4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))
for alunos in nome:
    media = (notas[a]+notas[b]+notas[c]+notas[d])/4
    print(f'\nAluno: {alunos}\nMedia: {media}')
    if media >= 7:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
    a += 4
    b += 4
    c += 4
    d += 4


     






        




