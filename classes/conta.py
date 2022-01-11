from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta 
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.informacoes()

    def informacoes(self):
        print(f'Agencia: {self.agencia}\n'
              f'Conta: {self.conta}\n'
              f'Saldo: R$ {self.saldo:.2f}\n')

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Você não possui saldo suficiente na conta.')
            return

        self.saldo -= valor
        self.informacoes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Você não possui saldo suficiente na conta.')
            return

        self.saldo -= valor
        self.informacoes()
