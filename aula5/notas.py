nota1 = float(input('digite nota1: '))
nota2 = float(input('digite nota2: '))
nota3 = float(input('digite nota3: '))
nota4 = float(input('digite nota4: '))

lista = {nota1, nota2, nota3, nota4}
print('A maior nota foi:', max(lista))
print('A menor nota foi:', min(lista))

resultado = (nota1 + nota2 + nota3 + nota4) / 4
print(f'\nMédia: {resultado}')

if resultado >= 7:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')


