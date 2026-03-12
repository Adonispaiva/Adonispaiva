"""Router de ingestão."""

from fastapi import APIRouter, Depends

from app.api.deps import get_ingest_document_use_case
from app.application.use_cases.ingest_archive import IngestArchiveUseCase
from app.application.use_cases.ingest_document import IngestDocumentUseCase
from app.infrastructure.parsing.zip_parser import ZipParser
from app.schemas.ingest import IngestArchiveRequest, IngestFileRequest, IngestFileResponse

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("/files", response_model=IngestFileResponse)
def ingest_file(
    payload: IngestFileRequest,
    use_case: IngestDocumentUseCase = Depends(get_ingest_document_use_case),
) -> IngestFileResponse:
    return use_case.execute(payload)


@router.post("/archives")
def ingest_archive(payload: IngestArchiveRequest) -> dict:
    use_case = IngestArchiveUseCase(parser=ZipParser())
    return use_case.execute(payload.archive_path)
