#Aula 4

num1 = int(input('digite um numero'))
num2 = int(input('digite mais um numero'))

print(f'Adição: {num1+num2}\nSubtracao: {num1-num2}\nMultiplicacao: {num1*num2}\nDivisao: {num1/num2}')

if num1 > num2:
    print('numero1 é maior')
elif num1 == num2:
    print("os numeros sao iguais")
else:
    print('"numero2 é maior"')


