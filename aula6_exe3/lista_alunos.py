nome = []
notas = []
media = 0
a=0
b=1
c=2
d=3

for i in range(0,3):
    nome.append(input(f'Digite o nome do aluno: '))
    for j in range(0,4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))

for alunos in nome:
    media = (notas[a]+notas[b]+notas[c]+notas[d])/4
    print(f'\nAluno: {alunos}\nMédia: {media}')
    if media >= 7:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
    a=a+4
    b=b+4
    c=c+4
    d=d+4
