lista = []
lista2 = ['Marcela', 'Nicole', '*Matheus', 10]
lista3 = [1, 2, 3, 5]


print(lista)
print(lista2)
print(lista3)



lista.append(lista2)
lista.append(lista3)
print(lista)

lista_perguntas = [input('Digite seu artista favorito'), input('Digite seu guitarrista favorito')]
print(lista_perguntas)

posicao = int(input('Digite a posicao: '))
print(lista2[posicao-1])

