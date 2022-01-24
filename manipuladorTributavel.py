
class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()

        return total

if __name__ == '__main__':
    from conta import ContaCorrente
    from tributavel import TributavelMixIn
    from seguraDeVida import SeguroDeVida


    cc1 = ContaCorrente("123", "Cleive", 1000)
    cc2 = ContaCorrente("345", "Chambule", 2000)

    seguro1 = SeguroDeVida(100,"Cleive", "324-6")
    seguro2 = SeguroDeVida(200, "Chambule", "234-0")

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)




