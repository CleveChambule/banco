import datetime

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data de Abertura: {}".format(self.data_abertura))
        print("Transacoes")
        for t in self.transacoes:
            print(" - ", t)