import csv
from collections.abc import MutableSequence

class Poupanca(MutableSequence):
    _poupanca = []

    def __len__(self):
        return len(self._poupanca)

    def __getitem__(self, posicao):
        return self._poupanca[posicao]

    def __setitem__(self, posicao, valor):
        self._poupanca[posicao] = valor

    def insert(self, posicao, valor):
        return self._poupanca.insert(posicao,valor)

    def __delitem__(self, posicao):
        del self._poupanca[posicao]