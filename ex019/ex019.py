import numpy as np

def calc_roots(a, b, c):
    delta = b**2 - 4*a*c  # Calcula o valor do discriminante

    if delta < 0:  # Não há raízes reais
        return ()
    elif delta == 0:  # Raiz unica
        x = -b / (2*a)
        return (x,)
    else:  # Duas raízes
        delta_root = np.sqrt(delta)
        x1 = (-b + delta_root) / (2*a)
        x2 = (-b - delta_root) / (2*a)
        return x1, x2

# Entrada dos coeficientes
a = float(input('Entre com o valor de A: '))
b = float(input('Entre com o valor de B: '))
c = float(input('Entre com o valor de C: '))

roots = calc_roots(a, b, c)
if not roots:
    print('Não há raízes reais')
elif len(roots) == 1:
    print(f'A função tem apenas uma raiz: {roots[0]}')
else:
    print(f'As raízes são: {roots}')