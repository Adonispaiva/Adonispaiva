"""Entidade de memória operacional."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class MemoryRecord(BaseModel):
    memory_id: str
    memory_scope: Literal["session", "project", "institutional", "user"]
    subject_id: str
    project: str | None
    summary: str
    evidence_doc_ids: list[str]
    confidence: float
    ttl_seconds: int | None
    created_at: datetime
    updated_at: datetime
    revocable: bool
