import csv
from collections.abc import MutableSequence

from cliente import Cliente
from conta import Conta, ContaPoupanca


class Poupanca(MutableSequence):
    _poupanca = []

    def __len__(self):
        return len(self._poupanca)

    def __getitem__(self, posicao):
        return self._poupanca[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Conta):
            self._poupanca[posicao] = valor
        else:
            raise TypeError("Valor invalido! Nao corresponde a uma conta")

    def insert(self, posicao, valor):
        if isinstance(valor, Conta):
            return self._poupanca.insert(posicao,valor)
        else:
            raise TypeError("Valor invalido! Nao corresponde a uma conta")

    def __delitem__(self, posicao):
        del self._poupanca[posicao]


if __name__ == "__main__":
    poupanca = Poupanca()

    arquivo = open("contas_poupancas.txt", "r")
    leitor = csv.reader(arquivo)

    for i in leitor:
        cliente = Cliente(i[1],i[2],i[3])
        conta = ContaPoupanca(int(i[0]),cliente,float(i[4]))
        print(conta)