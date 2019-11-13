#Estruturas de repeticao - FOR

#--- for simples usando range com incremento padrao de 1
for i in range(0,10,):
    print(f'{i}-nathan')

#--- for usando range com incremento de 2
for i in range(0,100,2):
    print(f'{i}- Pares')

#--- For em lista usando range
lista = ['mateus','matheus', 'marcela', 'nicole','tonho','pablo']
for i in range(0,6):
    print(lista[i])
#--- Exemplificando o problema do uso de for en lista usando range
lista.append('Natan')
for sortudo in lista:
    print(sortudo)

#--- For usando os elementos da própria lista 
numero = 10
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero} ')


    

