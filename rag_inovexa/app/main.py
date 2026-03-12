"""Entrypoint FastAPI do serviço RAG Inovexa."""

from fastapi import FastAPI

from app.api.routers import admin, catalog, evals, governance, health, ingest, memory, query
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.infrastructure.db.models import Base
from app.infrastructure.db.session import engine

settings = get_settings()
configure_logging(settings)

app = FastAPI(title=settings.app_name, debug=settings.app_debug)


@app.on_event("startup")
def on_startup() -> None:
    # Bootstrap inicial: create_all garante schema mínimo executável no primeiro setup.
    # Alembic deve evoluir para a fonte formal de migrações e gestão de schema.
    Base.metadata.create_all(bind=engine)


app.include_router(health.router)
app.include_router(ingest.router, prefix=settings.api_prefix)
app.include_router(query.router, prefix=settings.api_prefix)
app.include_router(catalog.router, prefix=settings.api_prefix)
app.include_router(memory.router, prefix=settings.api_prefix)
app.include_router(governance.router, prefix=settings.api_prefix)
app.include_router(evals.router, prefix=settings.api_prefix)
app.include_router(admin.router, prefix=settings.api_prefix)
