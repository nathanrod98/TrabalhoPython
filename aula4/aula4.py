#Aula 4

num1 = int(input('digite um numero'))
num2 = int(input('digite mais um numero'))

resultado = num1 + num2
print(resultado)
resultado = num1 - num2
print(resultado)
resultado = num1 * num2
print(resultado)
resultado = num1 / num2
print(resultado)

if num1 > num2:
    print('numero1 é maior')
elif num1 == num2:
    print("os numeros sao iguais")
else:
    print('numero2 é maior')


