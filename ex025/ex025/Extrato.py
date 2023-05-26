import datetime

class Extrato:
    def __init__(self, conta=None):
        self.conta = conta
        self.transacoes = []

    def imprimir(self, numeroconta):
        print(f'Extrato: {numeroconta}')
        for p in self.transacoes:
            print(f'{p[0]} {p[1]} {p[2]} {p[3]}')
