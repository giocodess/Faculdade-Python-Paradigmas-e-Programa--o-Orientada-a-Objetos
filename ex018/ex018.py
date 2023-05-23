def isPrime(n):
    if n <= 1:  # Números menores ou iguais a 1 não são primos
        print(f'{n} não é um número primo')
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f'{n} não é um número primo')
            return

    print(f'{n} é um número primo')

isPrime(eval(input(f'Digite o numero para saber se é primo ou não: ')))
