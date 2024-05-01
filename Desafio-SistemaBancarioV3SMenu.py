from abc import ABC, classmethod, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self, numero,cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self)->float:
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor>0 and valor<= self._saldo:
            self._saldo -= valor
            print("\nSaque realizado!")
        elif valor<=0:
            print("\nValor inválido!")
        else:
            print("\nSaldo insuficiente!")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito feito!")
            return True
        print("Valor inválido!")
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite =500, limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self,valor):
        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao["tipo"]=="Saque"])
        excedeu_limite = valor >self._limite
        excedeu_limite_saques = self._limite_saques <= numero_saques

        if excedeu_limite:
            print("Falha na operação! O valor excede o limite disponivel! ")
        elif excedeu_limite_saques:
            print("Falha na operação! Limite de saques atingido!")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self) -> str:
        return f"\nNome: {self._cliente}\nAgência: {self._agencia}\nCC: {self._numero}"
 
class Cliente:
    def __init__(self,endereco) -> None:
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome 
        self._data_nascimento = data_nascimento

class Transacao(ABC):
    @classmethod
    @abstractmethod
    def registrar(self,conta):
        pass

    @property
    @classmethod
    @abstractmethod
    def valor(self):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_valida = conta.sacar(self.valor)

        if transacao_valida:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        transacao_valida = conta.depositar(self.valor)

        if transacao_valida:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )

    @property
    def transacoes(self):
        return self._transacoes
