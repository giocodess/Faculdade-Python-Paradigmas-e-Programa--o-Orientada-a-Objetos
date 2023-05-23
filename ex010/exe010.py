arrayList = [10, 2, 5, 7, 6, 3]
even = []                   ##faço uma lista para armazenar os numeros pares


for num in arrayList:       ##para cada num na arrayList 
    if num % 2 == 0:        ##se o numero for divisivel por dois e tiver resto igual a 0
        even.append(num)    ##append = eu coloco um elemento passado dentro da funcao pra 
                            ##dentro de uma variavel passada antes do ponto 

soma = sum(even)            ##utilizo da função soma que existe em python pra somar os
                            ##itens do array even
print(f'os numeros pares são: {soma}')





