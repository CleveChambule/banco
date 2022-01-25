
class ManipuladorDeTributaveis:

    #verificamos se uma classe e tributavel ou nao
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            #verificacao do objecto
            if isinstance(t,Tributavel):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), "nao e tributavel")
        return total

if __name__ == '__main__':
    from conta import ContaCorrente, ContaPoupanca, ContaInvestimento
    from tributavel import Tributavel
    from seguraDeVida import SeguroDeVida


    cc1 = ContaCorrente("123", "Cleive", 1000)
    cc2 = ContaCorrente("345", "Chambule", 2000)
    cc3 = ContaInvestimento("543", "Obed")
    cc3.deposita(500)
    seguro1 = SeguroDeVida(100,"Cleive", "324-6")
    seguro2 = SeguroDeVida(200, "Chambule", "234-0")

    #registamos a classes que tem ligacao com a classe tributavrl - evitando heranca multipla
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    Tributavel.register(ContaInvestimento)

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    lista_tributaveis.append(cc3)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)





