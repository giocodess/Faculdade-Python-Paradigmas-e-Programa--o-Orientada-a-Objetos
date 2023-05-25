while True:
    try:
        x = int(input(f'Insira um número: '))
        if x <= 0:
            print('Erro: O número inserido é menor ou igual a zero.')
        else:
            break
    except ValueError:
        print('Erro: o valor inserido é inválido. Por favor, informe um valor numérico.')

print('Informou:', x)
