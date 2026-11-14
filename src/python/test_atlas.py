from atlas import Atlas, BST, TabelaHash, inserir_lote_pelo_meio


def test_vazio():
    assert TabelaHash().buscar(1) is None
    assert BST().altura() == 0
    assert BST().consultar_periodo(0, 99999999) == []
    assert Atlas().buscar(1) is None


def test_duplicado_bloqueado():
    a = Atlas()
    assert a.abrir(1, "U", "C", 20260101) is True
    assert a.abrir(1, "U", "C", 20260101) is False
    assert a.total() == 1


def test_ausente_retorno_controlado():
    a = Atlas()
    assert a.alterar(99, "X", "y") is False
    assert a.cancelar(99, "y") is False


def test_historico_preserva_passado():
    a = Atlas()
    a.abrir(1, "U", "C", 20260101)
    a.alterar(1, "EM_ANDAMENTO", "assumido")
    a.cancelar(1, "duplicado")
    hist = a.buscar(1).listar_historico()
    assert [e[0] for e in hist] == ["CANCELAMENTO", "ALTERACAO", "ABERTURA"]
    assert a.buscar(1).situacao_atual() == "CANCELADA"
    assert a.alterar(1, "ABERTA", "depois de cancelar") is False
    assert len(a.buscar(1).listar_historico()) == 3


def test_hash_adverso_colisoes():
    h = TabelaHash(5, redimensiona=False)
    for k in (12, 17, 22, 27):
        h.inserir(k, k)
    assert h.maior_cadeia() == 4
    assert h.buscar(27) == 27


def test_hash_redimensiona_sem_perder_chaves():
    h = TabelaHash(7, redimensiona=True)
    for k in range(1, 201):
        h.inserir(k, k)
    assert h.fator_carga() <= 1.0
    assert all(h.buscar(k) == k for k in range(1, 201))


def test_bst_ordenada_vs_pelo_meio():
    itens = [((i, i), i) for i in range(1, 16)]
    a = BST()
    for chave, p in itens:
        a.inserir(chave, p)
    b = BST()
    inserir_lote_pelo_meio(b, itens, 0, len(itens) - 1)
    assert a.altura() == 15
    assert b.altura() == 4


def test_bst_duplicado_ignorado():
    b = BST()
    assert b.inserir((1, 1), 1) is True
    assert b.inserir((1, 1), 1) is False
    assert b.tamanho == 1


def test_periodo():
    a = Atlas()
    a.abrir(1, "U", "C", 20260105)
    a.abrir(2, "U", "C", 20260110)
    a.abrir(3, "U", "C", 20260205)
    protocolos = [s.protocolo for s in a.consultar_periodo(20260101, 20260131)]
    assert protocolos == [1, 2]


if __name__ == "__main__":
    testes = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in testes:
        t()
        print("OK  ", t.__name__)
    print("\n%d testes passaram." % len(testes))