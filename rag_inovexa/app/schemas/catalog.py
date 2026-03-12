"""Schemas de catálogo."""

from pydantic import BaseModel


class CatalogDocument(BaseModel):
    doc_id: str
    title: str
    project: str | None
    normative_status: str
    authority_level: int


class CatalogDocumentsResponse(BaseModel):
    items: list[CatalogDocument]
    total: int
