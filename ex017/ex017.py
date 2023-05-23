def fatorialRecursivo(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorialRecursivo(n-1)
numberUsu = eval(input(f'Digite o numero que vc deseja ver o fatorial: '))
print(f'O fatorial de {numberUsu} é {fatorialRecursivo(numberUsu)}')