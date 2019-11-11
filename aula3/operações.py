nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('digite sua idade: '))

print(f'nome: {nome} sobrenome: {sobrenome} idade: {idade}')

if idade < 18:
    print('não pode beber')
else:
    print('pode beber')


