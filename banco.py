from actualizadoDEcontas import ActualizadorDeContas
class Banco:


    def __init__(self, contas):
        self.contas = []

    def adiciona_conta(self, conta):
        self.contas.append(conta)


    def posicao_conta(self, numero):
        i = 0
        while i < len(self.contas):
            if numero == self.contas[i]._numero:
                print(self.contas[i])
            i += 1


    def listar_contas(self):
        total_contas = 0
        while total_contas < len(self.contas):
            total_contas += 1
        print(total_contas)

    def conta_roda(self,contas):
        actualiza = ActualizadorDeContas(0.01)
        for contas in self.contas:
            actualiza.roda(contas)

