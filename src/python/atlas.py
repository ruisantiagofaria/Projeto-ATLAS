# ===== 1. LISTA ENCADEADA: historico de cada solicitacao =====
class Evento:
    """No da lista: um acontecimento na vida da solicitacao."""

    def __init__(self, tipo, situacao, descricao, proximo=None):
        self.tipo = tipo
        self.situacao = situacao
        self.descricao = descricao
        self.proximo = proximo     


class Solicitacao:
    def __init__(self, protocolo, unidade, categoria, data):
        self.protocolo = protocolo
        self.unidade = unidade
        self.categoria = categoria
        self.data = data           
        self.historico = None       
        self.registrar_evento("ABERTURA", "ABERTA", "solicitacao criada")

    def registrar_evento(self, tipo, situacao, descricao):
        self.historico = Evento(tipo, situacao, descricao, self.historico)

    def situacao_atual(self):
        return self.historico.situacao

    def listar_historico(self):
        saida = []
        atual = self.historico
        while atual is not None:
            saida.append((atual.tipo, atual.situacao, atual.descricao))
            atual = atual.proximo
        return saida