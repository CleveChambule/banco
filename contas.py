import csv
from collections.abc import MutableSequence

from conta import Conta, ContaCorrente


class Contas(MutableSequence):

   _dados = []


   def __len__(self):
      return len(self._dados)

   def __getitem__(self, posicao):
      return self._dados[posicao]

   def __setitem__(self, posicao, valor):
      if isinstance(valor, Conta):
         self._dados[posicao] = valor
      else:
         raise TypeError("Valor atribuido nao e uma conta")

   def insert(self, posicao, valor):
      if isinstance(valor, Conta):
         return self._dados.insert(posicao,valor)
      else:
         raise TypeError("Valor atribuido nao e uma conta")

   def __delitem__(self, posicao):
      del self._dados[posicao]






if __name__ == "__main__":
   contas = Contas()

   arquivo = open("contas.txt", "r")
   leitor = csv.reader(arquivo)

   for linha in leitor:
      conta = ContaCorrente(linha[0], linha[1], float(linha[2]))


   arquivo.close()