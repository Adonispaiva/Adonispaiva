"""Dependências da camada de API."""

from app.application.use_cases.ingest_document import IngestDocumentUseCase
from app.application.use_cases.run_query import RunQueryUseCase
from app.domain.services.authority_resolution import AuthorityResolutionService
from app.domain.services.query_classification import QueryClassificationService
from app.infrastructure.indexing.hybrid_search import HybridSearch


def get_ingest_document_use_case() -> IngestDocumentUseCase:
    return IngestDocumentUseCase(authority_service=AuthorityResolutionService())


def get_run_query_use_case() -> RunQueryUseCase:
    return RunQueryUseCase(
        classifier=QueryClassificationService(),
        hybrid_search=HybridSearch(),
    )
