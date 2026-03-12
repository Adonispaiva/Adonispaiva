# rag_inovexa

Backend RAG institucional do GPT Inovexa 2.0 com arquitetura modular, governança documental e base para recuperação híbrida.

## Visão do serviço
- Ingestão de documentos e arquivos ZIP.
- Recuperação contextual por busca híbrida (lexical + semântica).
- Precedência documental explícita para reduzir regressões normativas.
- Separação entre memória operacional e corpus normativo.

## Requisitos
- Python 3.12+

## Stack
- FastAPI + Pydantic
- SQLAlchemy + Alembic
- PostgreSQL/pgvector (com abstração por portas)
- pytest

## Como subir localmente
```bash
cd rag_inovexa
python -m venv .venv
```

### Ativação do ambiente virtual (Unix/Linux)
```bash
source .venv/bin/activate
```

### Ativação do ambiente virtual (Windows)
```powershell
.venv\Scripts\activate
```

### Instalação e execução
```bash
pip install -e .
uvicorn app.main:app --reload
```

## Variáveis de ambiente
Copie `.env.example` para `.env` e ajuste valores conforme ambiente.

## Endpoints disponíveis
- `GET /health`
- `POST /v1/ingest/files`
- `POST /v1/ingest/archives`
- `POST /v1/query/retrieve`
- `GET /v1/catalog/documents`

## Estrutura de diretórios
A estrutura segue separação rígida em `app/domain`, `app/application`, `app/infrastructure`, `app/api`, `app/schemas`, `workers`, `docs/adr` e suítes de teste por tipo.

## Próximos passos
1. Conectar persistência real de documentos/chunks.
2. Implementar adapters de pgvector e BM25 reais.
3. Incluir pipeline de parsing para PDF/DOCX/XLSX e processamento assíncrono.
4. Expandir governança (quarentena, retenção e auditoria completa).
