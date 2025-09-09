class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Erro: O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if valor <= 0:
            print('Erro: O valor do saque deve ser positivo.')
        elif self._saldo >= valor:
            self._saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print(f'Saldo insuficiente. Saldo atual: R$ {self._saldo:.2f}')

    def consultar_saldo(self):
        print(f'Saldo da conta de {self.titular}: R$ {self._saldo:.2f}')
        return self._saldo
    
minha_conta = ContaBancaria('00123-4', 'Rodrigo Silva', 1500.00)
minha_conta.consultar_saldo()
print('----Operações----')
minha_conta.depositar(550.75)
minha_conta.sacar(300.00)
minha_conta.sacar(2000.00)
minha_conta.depositar(-50)

print('----Saldo Final----')
minha_conta.consultar_saldo()