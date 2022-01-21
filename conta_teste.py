from conta import Conta
from cliente import Cliente

cliente = Cliente("Cleve", "Chambule","1234j")
conta = Conta('123',cliente)
cliente1 = Cliente("Denise","234","2124A")

conta1 = Conta("543", cliente1)


#conta.transferir_para(cont1,20)
conta.deposita(1000)
conta1.deposita(1000)
conta.transferir_para(conta1, 1000)
conta.extracto()
conta.historico.imprime()
print(Conta.get_total_contas())
conta1.historico.imprime()

conta1.extracto()
