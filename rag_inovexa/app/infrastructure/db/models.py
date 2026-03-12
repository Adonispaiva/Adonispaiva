"""Modelos relacionais iniciais para o RAG Inovexa."""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class DocumentModel(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    source_path: Mapped[str] = mapped_column(String(512))
    source_kind: Mapped[str] = mapped_column(String(32))
    project: Mapped[str | None] = mapped_column(String(128), nullable=True)
    product: Mapped[str | None] = mapped_column(String(128), nullable=True)
    doc_family: Mapped[str] = mapped_column(String(128))
    doc_type: Mapped[str] = mapped_column(String(128))
    title: Mapped[str] = mapped_column(String(255))
    language: Mapped[str] = mapped_column(String(16), default="pt-BR")
    version: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="draft")
    normative_status: Mapped[str] = mapped_column(String(32), default="operational")
    authority_level: Mapped[int] = mapped_column(Integer, default=10)
    sensitivity_level: Mapped[str] = mapped_column(String(32), default="internal")
    privacy_class: Mapped[str] = mapped_column(String(32), default="none")
    risk_class: Mapped[str] = mapped_column(String(32), default="moderate")
    effective_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    supersedes: Mapped[list[str]] = mapped_column(JSON, default=list)
    superseded_by: Mapped[list[str]] = mapped_column(JSON, default=list)
    implementation_alignment: Mapped[str] = mapped_column(String(32), default="unknown")
    use_for_generation: Mapped[bool] = mapped_column(Boolean, default=True)
    use_for_memory: Mapped[bool] = mapped_column(Boolean, default=False)
    use_for_eval: Mapped[bool] = mapped_column(Boolean, default=True)
    checksum: Mapped[str] = mapped_column(String(128))

    chunks: Mapped[list["ChunkModel"]] = relationship(back_populates="document")


class ChunkModel(Base):
    __tablename__ = "chunks"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    doc_id: Mapped[str] = mapped_column(ForeignKey("documents.id"), index=True)
    project: Mapped[str | None] = mapped_column(String(128), nullable=True)
    doc_type: Mapped[str] = mapped_column(String(128))
    title: Mapped[str] = mapped_column(String(255))
    section_path: Mapped[str] = mapped_column(String(255))
    sequence: Mapped[int] = mapped_column(Integer)
    content: Mapped[str] = mapped_column(Text)
    token_count: Mapped[int] = mapped_column(Integer)
    chunk_strategy: Mapped[str] = mapped_column(String(64))
    authority_level: Mapped[int] = mapped_column(Integer, default=10)
    normative_status: Mapped[str] = mapped_column(String(32), default="operational")
    sensitivity_level: Mapped[str] = mapped_column(String(32), default="internal")
    retrieval_priority: Mapped[int] = mapped_column(Integer, default=0)
    embedding_model: Mapped[str] = mapped_column(String(128), default="unknown")
    lexical_terms: Mapped[list[str]] = mapped_column(JSON, default=list)
    heading_context: Mapped[list[str]] = mapped_column(JSON, default=list)
    use_for_generation: Mapped[bool] = mapped_column(Boolean, default=True)

    document: Mapped[DocumentModel] = relationship(back_populates="chunks")


class DocumentRelationModel(Base):
    __tablename__ = "document_relations"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    source_doc_id: Mapped[str] = mapped_column(String(64), index=True)
    target_doc_id: Mapped[str] = mapped_column(String(64), index=True)
    relation_type: Mapped[str] = mapped_column(String(32), index=True)


class IngestionJobModel(Base):
    __tablename__ = "ingestion_jobs"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    source_label: Mapped[str] = mapped_column(String(255))
    project: Mapped[str] = mapped_column(String(128))
    status: Mapped[str] = mapped_column(String(32), default="created")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class RetrievalTraceModel(Base):
    __tablename__ = "retrieval_traces"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    query_id: Mapped[str] = mapped_column(String(64), index=True)
    selected_collections: Mapped[list[str]] = mapped_column(JSON, default=list)
    conflicts_detected: Mapped[list[str]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class MemoryRecordModel(Base):
    __tablename__ = "memory_records"

    id: Mapped[str] = mapped_column(String(64), primary_key=True, default=lambda: str(uuid4()))
    memory_scope: Mapped[str] = mapped_column(String(32), index=True)
    subject_id: Mapped[str] = mapped_column(String(64), index=True)
    project: Mapped[str | None] = mapped_column(String(128), nullable=True)
    summary: Mapped[str] = mapped_column(Text)
    evidence_doc_ids: Mapped[list[str]] = mapped_column(JSON, default=list)
    confidence: Mapped[float] = mapped_column(Float)
    ttl_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    revocable: Mapped[bool] = mapped_column(Boolean, default=True)
