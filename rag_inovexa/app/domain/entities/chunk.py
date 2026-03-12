"""Entidade de chunk para recuperação."""

from pydantic import BaseModel


class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    project: str | None
    doc_type: str
    title: str
    section_path: str
    sequence: int
    content: str
    token_count: int
    chunk_strategy: str
    authority_level: int
    normative_status: str
    sensitivity_level: str
    retrieval_priority: int
    embedding_model: str
    lexical_terms: list[str]
    heading_context: list[str]
    use_for_generation: bool
