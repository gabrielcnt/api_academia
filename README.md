# API Academia (Exercicios)

API simples para gerenciar exercicios (lista em memória)

## Sobre

Endpoints pra listar, buscar, criar, atualizar e deletar exercicios.

## Como executar (Linux)

1. Criar e ativar virtualenv:
```
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependências:
```
pip install -r requirements.txt
```

3. Rodar:
```
python3 app.py
```

A API estará em http://127.0.0.1:5000

## Endpoints
- GET /exercicios — listar todos
- GET /exercicios/<id> — buscar por id
- GET /exercicio?nome=... — buscar por nome (query param `nome`)
- POST /exercicio — criar (JSON)
- PUT /exercicio/<id> — atualizar (JSON)
- DELETE /exercicio/<id> — deletar