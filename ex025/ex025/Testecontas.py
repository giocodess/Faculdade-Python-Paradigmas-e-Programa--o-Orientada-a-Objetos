from Clientes import Cliente
from Contas import Conta

# Criação de objetos Cliente
cliente1 = Cliente("123456789", "João", "Rua A, 123")
cliente2 = Cliente("987654321", "Maria", "Rua B, 456")

# Criação da conta
conta1 = Conta([cliente1, cliente2], 1, 0)

# Realiza operações na conta
conta1.depositar(1000)
conta1.sacar(100)

# Imprime o extrato da conta
conta1.extrato.imprimir(conta1.numero)

# Gera o saldo atual da conta
conta1.gerarSaldo()
