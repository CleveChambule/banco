import csv
from collections.abc import MutableSequence

from actualizadoDEcontas import ActualizadorDeContas
from cliente import Cliente
from conta import Conta, ContaCorrente


class Contas(MutableSequence):

   _dados = []

   #sem esses metodos e impossivel instanciar essa clase

   #garante o que retorne o tamanho da estrutura de dados
   def __len__(self):
      return len(self._dados)

   #garante que pegemos um objecto e uma determinada posicao
   def __getitem__(self, posicao):
      return self._dados[posicao]

   #garante que mudemos um determinado valor de um objecto e uma determinada posicao
   def __setitem__(self, posicao, valor):
      #verifica se o objeto a ser atribuído é umainstância	de Funcionario
      #caso nao seja lancamos uma excepcao
      if isinstance(valor, Conta):
         self._dados[posicao] = valor
      else:
         raise TypeError("Valor atribuido nao e uma conta")

   #garante o funcionamento do metodo append
   def insert(self, posicao, valor):
      #verifica se o objeto a ser atribuído é umainstância de Funcionario
      #caso nao seja lancamos uma excepcao
      if isinstance(valor, Conta):
         return self._dados.insert(posicao,valor)
      else:
         raise TypeError("Valor atribuido nao e uma conta")

   #garante que apaguemos um objecto e uma determina posicao
   def __delitem__(self, posicao):
      del self._dados[posicao]






if __name__ == "__main__":
   contas = Contas()

   arquivo = open("contas_criadas.txt", "r")
   leitor = csv.reader(arquivo)

   for linha in leitor:
      cliente = Cliente(linha[1],linha[2],linha[3],)
      conta = ContaCorrente(int(linha[0]),cliente,float(linha[4]))
      contas.append(conta)
      #print(conta.saldo)




   adc = ActualizadorDeContas(0.01)
   print("saldo_actual - saldo_actualizado")
   for i in contas:
      print("{}".format( adc.roda(i)))