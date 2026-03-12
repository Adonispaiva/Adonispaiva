"""Router de catálogo documental."""

from fastapi import APIRouter

from app.schemas.catalog import CatalogDocument, CatalogDocumentsResponse

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.get("/documents", response_model=CatalogDocumentsResponse)
def list_documents() -> CatalogDocumentsResponse:
    items = [
        CatalogDocument(
            doc_id="doc-master-1",
            title="Documento Mestre do Projeto",
            project="gpt-inovexa",
            normative_status="canonical",
            authority_level=3,
        )
    ]
    return CatalogDocumentsResponse(items=items, total=len(items))
