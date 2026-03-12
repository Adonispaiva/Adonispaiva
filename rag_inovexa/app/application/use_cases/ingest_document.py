"""Caso de uso de ingestão de documento."""

from dataclasses import dataclass
from hashlib import sha256
from uuid import uuid4

from app.domain.services.authority_resolution import AuthorityContext, AuthorityResolutionService
from app.schemas.ingest import IngestFileRequest, IngestFileResponse


@dataclass
class IngestDocumentUseCase:
    """Valida e transforma um input de ingestão em registro lógico inicial."""

    authority_service: AuthorityResolutionService

    def execute(self, payload: IngestFileRequest) -> IngestFileResponse:
        checksum = sha256(
            f"{payload.source_label}:{payload.project}:{payload.normative_status}".encode()
        ).hexdigest()
        authority_level = self.authority_service.resolve_level(
            AuthorityContext(
                normative_status=payload.normative_status,
                authority_override=payload.authority_override,
            )
        )
        return IngestFileResponse(
            job_id=str(uuid4()),
            document_id=str(uuid4()),
            authority_level=authority_level,
            checksum=checksum,
            status="published" if payload.publish_after_validation else "accepted",
        )
