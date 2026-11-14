from atlas import Solicitacao, TabelaHash

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