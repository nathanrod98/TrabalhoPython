#--- Exercício 1 - Listas
#--- Escreva programa que leia o nome de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima a lista
lista = []
for i in range(0,10):
    lista.append(input('digite um nome')) 
for i in lista:
    print(i)