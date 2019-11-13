produto = input('digite o nome do produto: ')
categoria = int(input('digite a categoria do produto: 1- Alcoolico 2- Não Alcoolico'))

if categoria == 1:
    print(f'\nProduto: {produto}\nCategoria: Alcoolico')
else:
    print(f'\nProduto: {produto}\nCategoria: Não Alcoolico')