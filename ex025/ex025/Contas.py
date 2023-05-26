import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato(conta=self)  # Passa a própria conta como parâmetro para o extrato
        self.historico = ['abertura: ' + str(datetime.date.today()) + '\n']

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return f'Não existe saldo suficiente, seu saldo é de: {self.saldo}'
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transferencia(self, valor, contaDestinataria):
        if valor > self.saldo:
            return f'Não existe saldo suficiente, seu saldo é de: {self.saldo}'
        else:
            contaDestinataria.depositar(valor)
            self.saldo -= valor
            return f'Sua transferência foi realizada. O valor da transferência foi de: {valor}'
    
    def gerarSaldo(self):
        print(f'O número da conta é {self.numero} e seu saldo atual é de: {self.saldo}')
