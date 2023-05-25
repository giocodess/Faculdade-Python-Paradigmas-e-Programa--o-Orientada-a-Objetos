##implementar uma solução em Python que identifique se o numero digitado é ou não um numero

def inputCheck(inputUsu):
    if(validator.isdigit()):
        print(f'Parabéns, você inseriu um numero')
    else:
        print(f'Você não inseriu um numero, por favor tente novamente')

validator = input(f'Insira um numero: ')
inputCheck(validator)