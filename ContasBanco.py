from datetime import datetime
import pytz


class ContaCorrente:
    """
    Cria um objeto Conta-Corrente para gerenciar contas de clientes.

    Atributos:
        nome: Nome do Cliente <str>
        cpf: cpf do Cliente, <str>
        saldo: Saldo disponível <float>
        chequeES: Cheque Especial do Cliente <float>
        transacoes: Lista de transações da conta do Cliente <list of tuple(operator, saldo, date and time)>
    """

    @staticmethod
    def _data():
        fuso_br = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._chequeES = 500
        self._transacoes = []
        self._cartao = []

    def consultar_saldo(self):
        print(f'O seu saldo é de R$ {self._saldo:,.2f}')
        if 0 > self._saldo >= (self._chequeES * (-1)):
            print('Você está utilizando R$ {} do seu Cheque Especial!'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((f'+ R$ {valor:,.2f}', f'R$ {self._saldo:,.2f}', ContaCorrente._data()))

    def saque(self, valor):
        if valor <= (self._saldo + self._chequeES):
            self._saldo -= valor
            self._transacoes.append((f'- R$ {valor:,.2f}', f'R$ {self._saldo:,.2f}', ContaCorrente._data()))
        else:
            print('Você não tem saldo suficiente!')

    def hist_transacoes(self):
        print('Histórico de Transações')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saque(valor)
        conta_destino.depositar(valor)

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self. telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def check_agencia(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R$ {:,.2f}'.format(self.caixa))
        else:
            print('O valor de caixa está ok. Caixa atual: R$ {:,.2f}'.format(self.caixa))

    def emprestimo(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não disponível!')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))