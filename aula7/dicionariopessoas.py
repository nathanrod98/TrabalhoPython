lista_jogadores=[]
for i in range(1,3):
    jogador = {'Nome':'', 'Posicao':'', 'Numero':'','PernaBoa':''}
    jogador['Nome'] = input('Digite o nome: ')
    jogador['Posicao'] = input('Digite a posicao: ')
    jogador['Numero'] = input('Digite o numero: ')
    jogador['PernaBoa'] = input('Digite a Perna boa: ')
    lista_jogadores.append(jogador)
for lista in lista_jogadores:
    for x,y in lista.items():
        print(x,y)


