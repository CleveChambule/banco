from cliente import Cliente
from conta import ContaCorrente

class CaixaElectronico:

    contas = []
    def depositar(self, valor, conta):
        conta.deposita(valor)

    def saca(self, valor, conta):
        conta.saca(valor)

if __name__ == "__main__":
    def mensagem_inicial():
        print("Bem-vindo Ao Caixa-Electronico De Laulane \n")
        print("1 - Para Criar Conta-Corrente")
        print("2 - Para Criar Conta-Poupanca")

    def opcao_contas():
        opc = int(input("Digite a opcao: "))
        return opc


    def escolha_conta():
        opcao = int(input("Digite a opcao: "))
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
                    CaixaElectronico.contas.append(cc)
                elif opcao == 2:
                    cp = ContaPoupanca(numero, cl)
                    #contas.append(cp)
                    CaixaElectronico.contas.append(cc)
                return CaixaElectronico.contas
                break
            except ValueError:
                print("Digite os dados corretos!!!")

    def depositos():
        cont = escolha_conta()
        conta = cont[0]
        caixa = CaixaElectronico()
        valor = int(input("Digite o valor que pretende depositar: "))
        caixa.depositar(valor, conta)

    def imprimir():
        print(CaixaElectronico.contas[0])


    def menu(opcao):
        switcher = {
            1:  mensagem_inicial(),
            2:  depositos(),
            3: imprimir(),
        }
        return switcher.get(opcao, "Opcao invalida")


    op = opcao_contas()
    menu(op)




