# FastAPI Zero

Projeto de estudo do framework FastAPI seguindo o padrão AAA (Arrange-Act-Assert) para testes. Template completo para APIs RESTful com banco de dados SQLAlchemy, autenticação e testes automatizados.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido para construção de APIs
- **SQLAlchemy** - ORM para gerenciamento de banco de dados
- **Pydantic** - Validação de dados e settings
- **Alembic** - Migrações de banco de dados
- **Pytest** - Framework de testes (padrão AAA)
- **Pytest-cov** - Cobertura de testes
- **Ruff** - Linter e formatador de código Python
- **Taskipy** - Gerenciador de tarefas
- **Poetry** - Gerenciamento de dependências e ambiente virtual

## 📋 Pré-requisitos

- Python >= 3.13
- Poetry (gerenciador de dependências)
- Git (para clonar o repositório)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd Curso_FastAPI
```

2. Instale as dependências (com Poetry):
```bash
poetry install
```

3. Variáveis de ambiente
- Crie um arquivo `.env` na raiz (se necessário) com chaves como:
```
APP_ENV=development
PORT=8000
```
- O projeto usa pydantic/fastapi para carregar configurações a partir do ambiente (ver arquivo de configuração).

## ▶️ Executando a aplicação

Recomenda-se entrar no ambiente virtual do Poetry antes de rodar os comandos:
```bash
poetry shell
```

Após ativar o shell do Poetry, iniciar em modo de desenvolvimento com o CLI do FastAPI:
```bash
fastapi dev fastapi_zero/app.py
```

Alternativa com Uvicorn (sem usar `poetry shell`):
```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Ou usando Taskipy (se configurado nas tasks):
```bash
poetry run task start
```

Acesse a documentação automática:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testes

Executar todos os testes:
```bash
poetry run pytest -q
```

Rodar testes com cobertura (exemplo):
```bash
poetry run pytest --cov=app --cov-report=term
```

Princípio de testes: usar padrão AAA (Arrange, Act, Assert) e testes pequenos e determinísticos.

## 🧹 Lint e formatação

Formatar o código com Ruff:
```bash
poetry run ruff format .
```

Verificar problemas com Ruff:
```bash
poetry run ruff check .
```

Sugestão: adicione hooks de pré-commit para rodar ruff antes de commits.

## ⚙️ Tarefas (Taskipy)

Exemplos de tarefas (configuradas em pyproject.toml):
- start — inicia a aplicação em dev
- test — executa pytest
- lint — executa ruff check
- format — executa ruff format

Executar uma task:
```bash
poetry run task <nome-da-task>
# ex: poetry run task test
```

## 📁 Estrutura sugerida do projeto

Exemplo de layout:
```
fastapi_zero/
├─ app/
│  ├─ main.py
│  ├─ api/
│  │  └─ v1/
│  ├─ core/
│  │  └─ config.py
│  ├─ schemas/
│  ├─ services/
│  └─ tests/
│     ├─ unit/
│     └─ integration/
├─ pyproject.toml
├─ README.md
└─ .env.example
```

## 🔎 Exemplos de uso (cURL)

GET simples:
```bash
curl -s http://localhost:8000/health
# {"status":"ok"}
```

POST exemplo:
```bash
curl -X POST http://localhost:8000/items \
    -H "Content-Type: application/json" \
    -d '{"name":"teste","price":9.9}'
```

## Contribuição

- Abra issues para bugs ou melhorias.
- Fork -> branch -> pull request.
- Mantenha testes cobrindo mudanças e siga o padrão AAA.

---

Se precisar, atualize instruções de execução (porta, variáveis de ambiente) conforme sua configuração local.