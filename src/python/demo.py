from atlas import Solicitacao, TabelaHash, BST, inserir_lote_pelo_meio

s = Solicitacao(1001, "Maua", "TI", 20260105)
s.registrar_evento("ALTERACAO", "EM_ANDAMENTO", "atendente assumiu")
s.registrar_evento("CANCELAMENTO", "CANCELADA", "pedido duplicado")

print("Situacao atual:", s.situacao_atual())
for evento in s.listar_historico():
    print(evento)



    print("\n--- Tabela hash ---")
tabela = TabelaHash(7)
s1 = Solicitacao(1001, "Maua", "TI", 20260105)
s2 = Solicitacao(1002, "Maua", "RH", 20260110)
print("inserir 1001:", tabela.inserir(1001, s1))
print("inserir 1002:", tabela.inserir(1002, s2))
print("inserir 1001 de novo:", tabela.inserir(1001, s1))
print("buscar 1002:", tabela.buscar(1002).categoria)
print("buscar 9999:", tabela.buscar(9999))

print("\n--- Teste adverso: colisoes ---")
adversa = TabelaHash(5, redimensiona=False)
for chave in (12, 17, 22, 27):
    adversa.inserir(chave, chave)
print("maior cadeia:", adversa.maior_cadeia())

print("\n--- 200 protocolos, 7 baldes iniciais ---")
sem = TabelaHash(7, redimensiona=False)
com = TabelaHash(7, redimensiona=True)
for protocolo in range(1, 201):
    sem.inserir(protocolo, protocolo)
    com.inserir(protocolo, protocolo)
print("sem redimensionar: m=%d fator=%.2f maior cadeia=%d" % (sem.m, sem.fator_carga(), sem.maior_cadeia()))
print("com redimensionar: m=%d fator=%.2f maior cadeia=%d" % (com.m, com.fator_carga(), com.maior_cadeia()))

print("\n--- BST: consulta por periodo ---")
arvore = BST()
arvore.inserir((20260105, 1001), 1001)
arvore.inserir((20260110, 1002), 1002)
arvore.inserir((20260120, 1003), 1003)
arvore.inserir((20260210, 1004), 1004)
print("protocolos de 01/01 a 31/01:", arvore.consultar_periodo(20260101, 20260131))
print("inserir (20260105, 1001) de novo:", arvore.inserir((20260105, 1001), 1001))

print("\n--- BST: lote ordenado da migracao ---")
itens = [((20260101 + i, 2000 + i), 2000 + i) for i in range(15)]
ingenua = BST()
for chave, protocolo in itens:
    ingenua.inserir(chave, protocolo)
balanceada = BST()
inserir_lote_pelo_meio(balanceada, itens, 0, len(itens) - 1)
print("15 registros em ordem  -> altura", ingenua.altura())
print("15 registros pelo meio -> altura", balanceada.altura())