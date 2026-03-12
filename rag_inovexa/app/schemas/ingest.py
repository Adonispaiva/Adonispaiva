"""Schemas de ingestão."""

from pydantic import BaseModel, Field


class IngestFileRequest(BaseModel):
    source_label: str
    project: str
    source_tier: str
    normative_status: str
    authority_override: int | None = None
    sensitivity_override: str | None = None
    publish_after_validation: bool = False


class IngestFileResponse(BaseModel):
    job_id: str
    document_id: str
    authority_level: int
    checksum: str
    status: str = Field(default="accepted")


class IngestArchiveRequest(BaseModel):
    archive_path: str
