from historico import Historico
import abc
from tributavel import Tributavel
from saldoInsuficiente import SaldoInsuficiente

#classe abstrata - nao cria objectos
class Conta(abc.ABC):

    #ATRIBUTO DA CLASSE
    _total_contas = 0


    #construtor - com atributos do objecto
    def __init__(self, numero, cliente ,saldo = 0, limite = 1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()
        Conta._total_contas +=1

    #metodo para levantamento - com retorno
    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        elif self._saldo < valor:
            raise SaldoInsuficiente('Saldo insuficiente')
            self._saldo -= valor
            self.historico.transacoes.append("Levantamento de {}".format(valor))


    #metodo para depositar
    def deposita(self, valor):
        if valor < 0:
            #vai lancar um expecao
          raise ValueError("OPERACAO IMPOSSIVEL! Voce tentou depositar um valor negativo")
        else:
            self._saldo += valor
            self.historico.transacoes.append("Deposito no valor de {}".format(valor))


    #metodo para transferencia
    def transferir_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia mo valor de {} para conta {}".format(valor,destino._numero))
            return True

    #METODO GET - PARA RETORNAR O SALDO
    @property
    def saldo(self):
        return self._saldo

    #METODO SET - PARA ATRIBUIR UM VALOR AO SALDO
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo nao pode ser negativo")
        else:
            self._saldo = saldo

    #metodo para imprimir o extracto da conta
    def extracto(self):
        print("Conta: {} \nSaldo: {}".format( self._numero,self._saldo))

    #METODO ESTATICO USANDO UM ATRIBUTO DA CLASSE
    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    #metodo abstracto - que obriga as classes filhas a implementarem esse metodo
    @abc.abstractmethod
    def actualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo


    #METODO DE IMPRESSAO
    def __str__(self):
        return "Dados da conta: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero,self._titular,self._saldo,self._limite)




#CONTA CORRENTE - FILHA DA CONTA
class ContaCorrente(Conta):

    #atributo da classe
    _tipo = "Conta_Corrente"

    #metodo herdado obrigatoriamente da superclasse
    def actualiza(self,taxa):
        self._saldo = self._saldo * taxa * 2
        return self._saldo

    #metodo herdado da classe mae - com uma nova implementacao
    def deposita(self, valor):
        if valor < 0:
          raise ValueError("OPERACAO IMPOSSIVEL! Voce tentou depositar um valor negativo")
        else:
            self._saldo += + valor - 0.10

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo.')
        if self._saldo < valor:
            raise SaldoInsuficiente('Saldo Insuficiente')
        else:
            self._saldo -= valor
            self.historico.transacoes.append("Levantamento de {}".format(valor))



    def get_valor_imposto(self):
        return self._saldo * 0.01

    def __str__(self):
        return super().__str__() + "\nTipo de Conta: {}".format(ContaCorrente._tipo)

#CONTA POUPANCA - FILHA DA CONTA
class ContaPoupanca(Conta):

    _tipo = "Conta_Poupanca"

    def actualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo

    def deposita(self, valor):
        if valor < 0:
          raise ValueError("OPERACAO IMPOSSIVEL! Voce tentou depositar um valor negativo")
        else:
            self._saldo += + valor + 0.10

    def __str__(self):
        return super().__str__() + "\nTipo de Conta: {}".format(ContaPoupanca._tipo)


class ContaInvestimento(Conta):
    _tipo = "Conta_Investimento"
    def actualiza(self, taxa):
        self._saldo += self._saldo * taxa  * 5
        return self._saldo

    def get_valor_imposto(self):
        return self._saldo * 0.03

    def __str__(self):
        return super().__str__() + "\nTipo de Conta: {}".format(ContaInvestimento._tipo)



if __name__ == '__main__':
    from cliente import Cliente
    from actualizadoDEcontas import ActualizadorDeContas
    from banco import Banco

    """
    cliente1 = Cliente("Obed","Chambule","432J")
    cliente2 = Cliente("Betoel", "Chambule","431M")
    cliente3 = Cliente("Cleive", "Chambule", "870K")
    c1 = ContaCorrente("123",cliente1, 1000)
    c2 = ContaPoupanca("456",cliente2, 1000)
    c3 = ContaInvestimento(123,cliente3,2000)
    #adc = ActualizadorDeContas(0.01)
    contas = []
    banco = Banco(contas)
    banco.adiciona_conta(c1)
    banco.adiciona_conta(c2)
    banco.adiciona_conta(c3)
    #banco.posicao_conta("789")
    banco.conta_roda(contas)
    #adc.roda(c1)
    print(c2)
    """

    cc = ContaCorrente("9002", "Cleive", 1000)

    try:
        valor = 20
        cc.saca(valor)
        print("Levantamento de {} realizado com sucesso!".format(valor))
    except ValueError:
        print("O valor a ser sacado dever ser um numero positivo")
    except SaldoInsuficiente:
        print("Voce nao possui saldo suficiente para concluir esta operacao")

    cc.deposita(200)
    print(cc)



