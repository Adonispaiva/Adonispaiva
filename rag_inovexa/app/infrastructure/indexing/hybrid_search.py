"""Busca híbrida combinando sinais semânticos e lexicais."""


class HybridSearch:
    """Fusão de candidatos com pesos multi-fator."""

    def search(
        self,
        lexical_hits: list[dict],
        semantic_hits: list[dict],
        max_candidates: int,
    ) -> list[dict]:
        merged: dict[str, dict] = {}

        for hit in lexical_hits + semantic_hits:
            key = hit.get("chunk_id") or hit.get("doc_id")
            if key not in merged:
                merged[key] = hit.copy()
            else:
                merged[key].update({k: v for k, v in hit.items() if v is not None})

        ranked = []
        for item in merged.values():
            score = (
                0.35 * float(item.get("semantic_score", 0.0))
                + 0.25 * float(item.get("lexical_score", 0.0))
                + 0.15 * float(item.get("authority_score", 0.0))
                + 0.1 * float(item.get("recency_score", 0.0))
                + 0.1 * float(item.get("scope_match_score", 0.0))
                + 0.05 * float(item.get("document_role_score", 0.0))
            )
            item["final_score"] = round(score, 6)
            ranked.append(item)

        ranked.sort(key=lambda x: x["final_score"], reverse=True)
        return ranked[:max_candidates]
