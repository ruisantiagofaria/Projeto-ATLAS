from atlas import Solicitacao

s = Solicitacao(1001, "Maua", "TI", 20260105)
s.registrar_evento("ALTERACAO", "EM_ANDAMENTO", "atendente assumiu")
s.registrar_evento("CANCELAMENTO", "CANCELADA", "pedido duplicado")

print("Situacao atual:", s.situacao_atual())
for evento in s.listar_historico():
    print(evento)