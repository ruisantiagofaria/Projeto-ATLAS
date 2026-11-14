# Projeto ATLAS - IED001 (P2) - Grupo The Office

Proposta de organização de dados para a plataforma ATLAS, com protótipo em Python.
Usa lista encadeada, tabela hash e BST, cada uma com um papel diferente.

## Integrantes do grupo

-ANDERSON RODRIGUES SALES
-GABRIELY ALVIM DOS SANTOS FONSECA
-JOÃO VICTOR DOS SANTOS FERREIRA
-MATHEUS PERES DO NASCIMENTO
-RUI SANTIAGO FARIA


## Papel de cada estrutura

| Estrutura | Papel no ATLAS |
|---|---|
| Tabela hash (encadeamento) | índice por protocolo; localiza rápido e recusa protocolo repetido |
| Lista encadeada | histórico de eventos de cada solicitação; o passado nunca é alterado |
| BST | índice ordenado por (data de abertura, protocolo); consultas por período |

A classe `Atlas` junta as três estruturas.

## Como executar

Só usa a biblioteca padrão do Python.

- Demonstração: `py src/python/demo.py` 
- Testes: `py src/python/test_atlas.py` 

## Estrutura do repositório

- `src/python/atlas.py`: as três estruturas e a classe Atlas
- `src/python/demo.py`: cenários de demonstração
- `src/python/test_atlas.py`: 9 testes (vazio, duplicado, ausente, adverso, alteração)
- `docs/relatorio.pdf`: relatório do projeto
- `evidencias/`: saídas das execuções

## Premissas

- Protocolo é um número inteiro; data é um inteiro no formato AAAAMMDD.
- Protocolo e data de abertura não mudam depois da criação.
- Solicitação cancelada não aceita novas alterações.
- Tudo roda em memória (protótipo).
