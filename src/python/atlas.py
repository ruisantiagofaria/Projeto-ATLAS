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
    

    # ===== 2. TABELA HASH com encadeamento: protocolo -> Solicitacao =====
class NoHash:
    def __init__(self, chave, valor, proximo=None):
        self.chave = chave
        self.valor = valor
        self.proximo = proximo


class TabelaHash:
    def __init__(self, m=7, redimensiona=True):
        self.m = m                     
        self.baldes = [None] * m        
        self.tamanho = 0
        self.redimensiona = redimensiona

    def _h(self, chave):
        return chave % self.m           

    def fator_carga(self):
        return self.tamanho / self.m

    def buscar(self, chave):
        no = self.baldes[self._h(chave)]
        while no is not None:
            if no.chave == chave:
                return no.valor
            no = no.proximo
        return None

    def inserir(self, chave, valor):
        """Devolve False se a chave ja existe (bloqueia protocolo repetido)."""
        if self.buscar(chave) is not None:
            return False
        i = self._h(chave)
        self.baldes[i] = NoHash(chave, valor, self.baldes[i])  
        self.tamanho += 1
        if self.redimensiona and self.fator_carga() > 1.0:
            self._redimensionar()
        return True

    def _redimensionar(self):
        antigos = self.baldes
        self.m = self.m * 2 + 1         
        self.baldes = [None] * self.m
        for cabeca in antigos:          
            no = cabeca
            while no is not None:
                proximo = no.proximo
                i = self._h(no.chave)
                no.proximo = self.baldes[i]
                self.baldes[i] = no
                no = proximo

    def maior_cadeia(self):
        maior = 0
        for cabeca in self.baldes:
            tam = 0
            no = cabeca
            while no is not None:
                tam += 1
                no = no.proximo
            if tam > maior:
                maior = tam
        return maior

    # ===== 3. BST: indice ordenado por (data, protocolo) =====
class NoBST:
    def __init__(self, chave, protocolo):
        self.chave = chave          
        self.protocolo = protocolo
        self.esq = None
        self.dir = None


class BST:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, chave, protocolo):
        """Devolve False se a chave ja existe (duplicados ignorados)."""
        novo = NoBST(chave, protocolo)
        if self.raiz is None:
            self.raiz = novo
            self.tamanho = 1
            return True
        atual = self.raiz
        while True:
            if chave < atual.chave:
                if atual.esq is None:
                    atual.esq = novo
                    break
                atual = atual.esq
            elif chave > atual.chave:
                if atual.dir is None:
                    atual.dir = novo
                    break
                atual = atual.dir
            else:
                return False
        self.tamanho += 1
        return True

    def altura(self):
        if self.raiz is None:
            return 0
        maior = 0
        pilha = [(self.raiz, 1)]
        while pilha:
            no, nivel = pilha.pop()
            if nivel > maior:
                maior = nivel
            if no.esq is not None:
                pilha.append((no.esq, nivel + 1))
            if no.dir is not None:
                pilha.append((no.dir, nivel + 1))
        return maior

    def consultar_periodo(self, data_ini, data_fim):
        """Protocolos abertos entre data_ini e data_fim, em ordem de data."""
        saida = []
        self._periodo(self.raiz, data_ini, data_fim, saida)
        return saida

    def _periodo(self, no, d1, d2, saida):
        if no is None:
            return
        data = no.chave[0]
        if d1 <= data:                      
            self._periodo(no.esq, d1, d2, saida)
        if d1 <= data <= d2:
            saida.append(no.protocolo)
        if data <= d2:                      
            self._periodo(no.dir, d1, d2, saida)


def inserir_lote_pelo_meio(arvore, itens, ini, fim):
    """Para lotes ja ordenados: insere o elemento do meio primeiro e depois
    cada metade. `itens` e uma lista de (chave, protocolo) ordenada."""
    if ini > fim:
        return
    meio = (ini + fim) // 2
    chave, protocolo = itens[meio]
    arvore.inserir(chave, protocolo)
    inserir_lote_pelo_meio(arvore, itens, ini, meio - 1)
    inserir_lote_pelo_meio(arvore, itens, meio + 1, fim)