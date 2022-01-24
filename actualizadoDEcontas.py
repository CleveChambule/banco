class ActualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total


    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta.saldo))
        self._saldo_total += conta.actualiza(self._selic)
        print("Saldo Final: {}".format(self._saldo_total))