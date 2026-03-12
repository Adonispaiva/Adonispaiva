"""Caso de uso de recuperação contextual."""

from dataclasses import dataclass
from uuid import uuid4

from app.domain.services.query_classification import QueryClassificationService
from app.infrastructure.indexing.hybrid_search import HybridSearch
from app.schemas.query import CandidateChunk, RetrieveQueryRequest, RetrieveQueryResponse


@dataclass
class RunQueryUseCase:
    """Executa fluxo base de classificação e ranking híbrido."""

    classifier: QueryClassificationService
    hybrid_search: HybridSearch

    def execute(self, payload: RetrieveQueryRequest) -> RetrieveQueryResponse:
        query_type = self.classifier.classify(payload.question, payload.query_type_hint)
        selected_collections = ["institutional"]
        if payload.project:
            selected_collections.append(f"project:{payload.project}")
        if payload.need_memory:
            selected_collections.append("memory:operational")

        semantic_hits = [
            {
                "chunk_id": "chunk-sem-1",
                "doc_id": "doc-master-1",
                "title": "Documento Mestre",
                "semantic_score": 0.91,
                "lexical_score": 0.2,
                "authority_score": 0.95,
                "recency_score": 0.8,
                "scope_match_score": 1.0,
                "document_role_score": 1.0,
            }
        ]
        lexical_hits = [
            {
                "chunk_id": "chunk-lex-1",
                "doc_id": "doc-guide-1",
                "title": "Diretriz Operacional",
                "semantic_score": 0.5,
                "lexical_score": 0.82,
                "authority_score": 0.6,
                "recency_score": 0.7,
                "scope_match_score": 0.8,
                "document_role_score": 0.7,
            }
        ]

        ranked = self.hybrid_search.search(lexical_hits, semantic_hits, payload.max_candidates)
        conflicts = []
        if query_type == "normative_lookup" and payload.allow_historical:
            conflicts.append("historical_material_should_not_lead_generation")

        candidates = [
            CandidateChunk(
                chunk_id=item["chunk_id"],
                doc_id=item["doc_id"],
                score=item["final_score"],
                title=item.get("title", "untitled"),
            )
            for item in ranked[: payload.max_context_chunks]
        ]

        return RetrieveQueryResponse(
            query_id=str(uuid4()),
            selected_collections=selected_collections,
            candidates=candidates,
            recommended_context_bundle_id=f"ctx-{uuid4()}",
            conflicts_detected=conflicts,
        )
