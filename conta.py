from historico import Historico
import abc
from tributavel import TributavelMixIn

class Conta(abc.ABC):

    #ATRIBUTO DA CLASSE
    _total_contas = 0


    #construtor
    def __init__(self, numero, cliente ,saldo = 0, limite = 1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()
        Conta._total_contas +=1

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append("Levantamento de {}".format(valor))
            return True


    def deposita(self, valor):
        if valor > self._limite:
            print("OPERACAO IMPOSSIVEL! O seu limite de saldo e de {}".format(self._limite))
        else:
            self._saldo += valor
            self.historico.transacoes.append("Deposito no valor de {}".format(valor))

    def transferir_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia mo valor de {} para conta {}".format(valor,destino._numero))
            return True

    #METODO GET - PARA PEGAR
    @property
    def saldo(self):
        return self._saldo

    #METODO SET - PARA ATRIBUIR
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo nao pode ser negativo")
        else:
            self._saldo = saldo

    def extracto(self):
        print("Conta: {} \nSaldo: {}".format( self._numero,self._saldo))

    #METODO ESTATICO USANDO UM ATRIBUTO DA CLASSE
    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    @abc.abstractmethod
    def actualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo


    #METODO DE IMPRESSAO
    def __str__(self):
        return "Dados da conta: \nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}".format(self._numero,self._titular,self._saldo,self._limite)




#CONTA CORRENTE - FILHA DA CONTA
class ContaCorrente(Conta):

    _tipo = "Conta_Corrente"

    def actualiza(self,taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += self._saldo - 0.10

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

    def __str__(self):
        return super().__str__() + "\nTipo de Conta: {}".format(ContaPoupanca._tipo)


class ContaInvestimento(Conta):
    _tipo = "Conta_Investimento"
    def actualiza(self, taxa):
        self._saldo += self._saldo * taxa  * 5
        return self._saldo

    def __str__(self):
        return super().__str__() + "\nTipo de Conta: {}".format(ContaInvestimento._tipo)



if __name__ == '__main__':
    from cliente import Cliente
    from actualizadoDEcontas import ActualizadorDeContas
    from banco import Banco

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



