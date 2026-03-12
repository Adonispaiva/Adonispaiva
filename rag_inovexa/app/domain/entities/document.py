"""Entidade de documento normativo."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Document(BaseModel):
    doc_id: str
    source_path: str
    source_kind: Literal["file", "zip", "repo", "supervision", "manual"]
    project: str | None
    product: str | None
    doc_family: str
    doc_type: str
    title: str
    language: str
    version: str | None
    status: Literal["draft", "active", "frozen", "historical", "superseded", "quarantined"]
    normative_status: Literal[
        "sovereign", "normative", "canonical", "operational", "snapshot", "derived", "historical"
    ]
    authority_level: int
    sensitivity_level: Literal["public", "internal", "restricted", "sensitive", "critical"]
    privacy_class: Literal["none", "pii_low", "pii_medium", "pii_high"]
    risk_class: Literal["low", "moderate", "high", "critical"]
    effective_date: datetime | None
    updated_at: datetime | None
    supersedes: list[str]
    superseded_by: list[str]
    implementation_alignment: Literal["unknown", "planned", "partial", "aligned", "divergent"]
    use_for_generation: bool
    use_for_memory: bool
    use_for_eval: bool
    checksum: str
