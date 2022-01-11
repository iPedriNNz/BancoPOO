from classes.banco import Banco
from classes.cliente import Cliente
from classes.conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Pedro Luiz Ferreira', 24)
conta1 = ContaCorrente(1111, 123456, 200)
cliente1.inserir_conta(conta1)
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)


cliente2 = Cliente('Maria', 18)
conta2 = ContaCorrente(2222, 123457, 20)
cliente2.inserir_conta(conta2)
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

cliente3 = Cliente('João', 50)
conta3 = ContaPoupanca(1212, 123458, 0)
cliente3.inserir_conta(conta3)
banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(240)
else:
    print('Cliente não autenticado.')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(0)
    cliente3.conta.sacar(20)
else:
    print('Cliente não autenticado.')
