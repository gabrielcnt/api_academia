# API Academia (Exercicios)

API simples para gerenciar exercicios (lista em memória)

## Sobre

Endpoints pra listar, buscar, criar, atualizar e deletar exercicios.

## Como executar (Linux)

1. Criar e ativar virtualenv:
```
python3 -m venv venv
source venv/bin/activate

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
```


## Blueprints e Schemas

### Blueprints (`resource/`)
- **Local:** `resource/` — contains os blueprints registrados em `app.py`.
- **exercicios.py:** rotas `/exercicio` e `/exercicio/<id>`; métodos: GET (lista/detalhe), POST (criar), PUT (atualizar inteiro), PATCH (atualizar parcial), DELETE (remover).
- **aluno.py:** blueprint para rotas relacionadas a alunos (registro semelhante em `app.py`).

### Schemas (`schemas/`)
- **Local:** `schemas/` — validação e serialização com `marshmallow`.
- **exercicios.py:** campos: `id` (str), `nome` (str, obrigatório), `grupo_muscular` (str, obrigatório), `repeticoes` (int, >=1), `series` (int, >=1).
- **aluno.py:** schemas para validação de dados de alunos (ver `schemas/aluno.py`).

### Observações rápidas
- Blueprints são registrados em `app.py` com `api.register_blueprint(...)`.
- O decorator `@<blueprint>.arguments` desserializa o JSON e injeta o objeto como parâmetro do método (ex.: `def post(self, dado):`).
- Swagger (docs) disponível em `/docs` quando `flask-smorest` está configurado corretamente.

---

Documento curto e direto, alinhado ao estilo já presente acima.
