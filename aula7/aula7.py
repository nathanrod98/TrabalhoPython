
lista = []
dicionario = { ' Nome': 'Nathan', 'Sobrenome' : 'Rodrigues'}
print(dicionario)
print(dicionario['Sobrenome'])


nome = 'nathan'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome': nome, 'Lista_notas': lista_notas, 'Média': media, 'Situacao': situacao}

print(dicionario_alunos)

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")

print(f"{dicionario_alunos['Lista_notas']}")