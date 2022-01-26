from collections.abc import MutableSequence

from cliente import Cliente
from conta import ContaCorrente, Conta, ContaPoupanca
from saldoInsuficiente import SaldoInsuficiente


class CaixaElectronico(MutableSequence):

    _contas = []

    #Algo que podia importar
    def depositar(self, valor, conta):
        conta.deposita(valor)

    def saca(self, valor, conta):
        conta.saca(valor)
    # sem esses metodos e impossivel instanciar essa clase

    # garante o que retorne o tamanho da estrutura de dados
    def __len__(self):
        return len(self._contas)

    # garante que pegemos um objecto e uma determinada posicao
    def __getitem__(self, posicao):
        return self._contas[posicao]

    # garante que mudemos um determinado valor de um objecto e uma determinada posicao
    def __setitem__(self, posicao, valor):
        # verifica se o objeto a ser atribuído é umainstância	de Funcionario
        # caso nao seja lancamos uma excepcao
        if isinstance(valor, Conta):
            self._contas[posicao] = valor
        else:
            raise TypeError("Valor atribuido nao e uma conta")

    # garante o funcionamento do metodo append
    def insert(self, posicao, valor):
        # verifica se o objeto a ser atribuído é umainstância de Funcionario
        # caso nao seja lancamos uma excepcao
        if isinstance(valor, Conta):
            return self._contas.insert(posicao, valor)
        else:
            raise TypeError("Valor atribuido nao e uma conta")

    # garante que apaguemos um objecto e uma determina posicao
    def __delitem__(self, posicao):
        del self._contas[posicao]

if __name__ == "__main__":
    def mensagem_inicial():
        print("Bem-vindo Ao Caixa-Electronico De Laulane \n")
        print("1 - Para Criar Conta-Corrente")
        print("2 - Para Criar Conta-Poupanca")

    def opcao_contas():
        opc = int(input("Digite a opcao desejada: "))
        return opc


    def escolha_conta():
        mensagem_inicial()
        opcao = int(input("Digite a opcao desejada: "))
        cond = True
        #contas = []
        while cond:
            try:
                numero = int(input("Digite o numero: "))
                nome = input("Digite o nome: ")
                sobrenome = input("Digite o sobrenome: ")
                bi = input("Digite o numero de BI: ")
                cl = Cliente(nome, sobrenome, bi)
                if opcao == 1:
                    cc = ContaCorrente(numero, cl)
                    #contas.append(cc)
                    CaixaElectronico._contas.append(cc)
                elif opcao == 2:
                    cp = ContaPoupanca(numero, cl)
                    #contas.append(cp)
                    CaixaElectronico._contas.append(cp)
                return CaixaElectronico._contas
                break
            except ValueError:
                print("Digite os dados corretos!!!")

    def conta_criada():
        rec = CaixaElectronico._contas
        if len(rec) > 0:
            return True
        else:
            return False

    def depositos():
        cont = CaixaElectronico._contas
        #conta = cont[0]
        caixa = CaixaElectronico()
        valor = int(input("Digite o valor que pretende depositar: "))
        num = int(input("Digite o numero de conta: "))
        for conta in cont:
            if conta._numero == num:
                caixa.depositar(valor, conta)

    def levantamento():
        caixa = CaixaElectronico()
        valor = int(input("Digite o valor que pretende levantar: "))
        num = int(input("Digite o numero de conta: "))
        for conta in CaixaElectronico._contas:
            if conta._numero == num:
                if isinstance(conta, Conta.saca()):
                    caixa.saca(valor,conta)
                    print("Essa Conta nao esta auorizada a fazer levantamento")

    def imprimir():
        #print(CaixaElectronico.contas[0])
        for i in CaixaElectronico._contas:
            print(i)

    def historco_contas():
        hi = int(input("Qual e o numero de conta que pretende ver: "))

        for conta in CaixaElectronico._contas:
            if conta._numero == hi:
                conta.historico.imprime()



    def menu():
        cond = True
        escolha_conta()
        while cond:
            if conta_criada() == True:
                print("""
Bem-vindo Ao Caixa-Electronico De Laulane

1 - Para Criar Uma Conta!
2 - Para Fazer Deposito!
3 - Para Imprimir As Contas!
4 - Para Imprimir O Historico de Conta!
5 - Para Fazer Levantamento!
6 - Para Sair da Aplicacao!
                """)
                opcao = int(input("Digite a opcao: "))
                if opcao == 1:
                    escolha_conta()
                elif opcao == 2:
                    tr = True
                    while tr:
                        try:
                            depositos()
                            tr = False
                        except ValueError:
                            print("OPERACAO IMPOSSIVEL...VOCE TENTOU DEPOSITAR UM VALOR NEGATIVO")
                            tr = False
                elif opcao == 3:
                    imprimir()
                elif opcao == 4:
                    historco_contas()
                elif opcao == 5:
                    con = True
                    while con:
                        try:
                            levantamento()
                            con = False
                        except SaldoInsuficiente:
                            print("OPERCAO FALHOU...SALDO INSUFICINTE")
                            con = False
                        except ValueError:
                            print("OPERACAO IMPOSSIVEL...VOCE TENTOU LEVANTAR UM VALOR NEGATIVO")
                            con = False
                elif opcao == 6:
                    cond = False





menu()
