#VARIAVEIS
shoppingCart = eval(input(f'digite a quantidade de artes que você deseja: '))
i = shoppingCart*10
descount = 0
xdescount = 1.00

##ALGORITMO DE DESCONTO
if(shoppingCart <= 10):
    print(f'Valor Original: {i}R$')
    print(f'Não há descontos aplicáveis')
    print(f'Valor final: {i}R$')
elif shoppingCart <= 20 :
    descount = 0.10
    print(f'Valor Original: {i}R$')
    print(f'Valor do desconto: {i*descount}R$')
    print(f'Valor final {i*(xdescount-descount)}R$')
else:
    descount = 0.20
    print(f'Valor Original: {i}R$')
    print(f'Valor do desconto: {i*descount}R$')
    print(f'Valor final {i*(xdescount-descount)}R$')
