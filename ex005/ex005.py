# IMC TEST IMC = PESO/ALTURA
nameUsu = input(f'Para calcular seu IMC me diga seu nome: ')
weight = eval(input(f'{nameUsu} por favor, informe seu peso ex:"70": '))
height = eval(input(f'agora informe sua altura ex:"170": '))
imcUsu = weight/(height**2)

print(f'{nameUsu} seu IMC é de {imcUsu}')