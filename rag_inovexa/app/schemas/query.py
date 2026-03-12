"""Schemas de consulta e recuperação."""

from pydantic import BaseModel


class RetrieveQueryRequest(BaseModel):
    question: str
    project: str | None = None
    query_type_hint: str | None = None
    need_memory: bool = False
    max_candidates: int = 10
    max_context_chunks: int = 6
    allow_historical: bool = False
    sensitivity_mode: str = "internal"


class CandidateChunk(BaseModel):
    chunk_id: str
    doc_id: str
    score: float
    title: str


class RetrieveQueryResponse(BaseModel):
    query_id: str
    selected_collections: list[str]
    candidates: list[CandidateChunk]
    recommended_context_bundle_id: str
    conflicts_detected: list[str]
