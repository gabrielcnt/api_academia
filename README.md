# API Academia

API REST para gerenciar alunos e exercícios de academia.

## Sobre

Endpoints para criar, listar, buscar, atualizar e deletar alunos e exercícios.

## Instalação

1. **Criar e ativar virtualenv:**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

## Como Executar

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000`

## Documentação Interativa

Acesse a documentação Swagger UI em: `http://127.0.0.1:5000/docs`

## Banco de Dados

A API utiliza SQLite. O banco de dados é armazenado em `instance/data.db`

Para resetar o banco, delete o arquivo `instance/data.db` e reinicie a aplicação.

## Endpoints

### Alunos

- **GET** `/alunos` — Listar todos os alunos
- **POST** `/alunos` — Criar novo aluno
- **GET** `/alunos/<id>` — Buscar aluno por ID
- **PUT** `/alunos/<id>` — Atualizar aluno
- **DELETE** `/alunos/<id>` — Deletar aluno

### Exercícios

- **GET** `/exercicio` — Listar todos os exercícios
- **POST** `/exercicio` — Criar novo exercício
- **GET** `/exercicio/<id>` — Buscar exercício por ID
- **PUT** `/exercicio/<id>` — Atualizar exercício completamente
- **PATCH** `/exercicio/<id>` — Atualizar exercício parcialmente
- **DELETE** `/exercicio/<id>` — Deletar exercício

## Exemplos de Requests

### Criar Aluno
```bash
curl -X POST http://localhost:5000/alunos \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "idade": 25,
    "cpf": 12345678901
  }'
```

**Resposta (201):**
```json
{
  "id": 1,
  "nome": "João Silva",
  "idade": 25,
  "cpf": 12345678901,
  "exercicio": []
}
```

### Listar Alunos
```bash
curl -X GET http://localhost:5000/alunos
```

### Buscar Aluno por ID
```bash
curl -X GET http://localhost:5000/alunos/1
```

### Atualizar Aluno
```bash
curl -X PUT http://localhost:5000/alunos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Santos",
    "idade": 26,
    "cpf": 12345678901
  }'
```

### Deletar Aluno
```bash
curl -X DELETE http://localhost:5000/alunos/1
```

### Criar Exercício
```bash
curl -X POST http://localhost:5000/exercicio \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Supino",
    "grupo_muscular": "Peito",
    "series": 4,
    "repeticoes": 10,
    "aluno_id": 1
  }'
```

**Resposta (201):**
```json
{
  "id": 1,
  "nome": "Supino",
  "grupo_muscular": "Peito",
  "series": 4,
  "repeticoes": 10,
  "aluno_id": 1
}
```

### Listar Exercícios
```bash
curl -X GET http://localhost:5000/exercicio
```

### Buscar Exercício por ID
```bash
curl -X GET http://localhost:5000/exercicio/1
```

### Atualizar Exercício (PUT)
```bash
curl -X PUT http://localhost:5000/exercicio/1 \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Supino Inclinado",
    "grupo_muscular": "Peito",
    "series": 3,
    "repeticoes": 12,
    "aluno_id": 1
  }'
```

### Atualizar Parcialmente (PATCH)
```bash
curl -X PATCH http://localhost:5000/exercicio/1 \
  -H "Content-Type: application/json" \
  -d '{
    "repeticoes": 15
  }'
```

### Deletar Exercício
```bash
curl -X DELETE http://localhost:5000/exercicio/1
```
