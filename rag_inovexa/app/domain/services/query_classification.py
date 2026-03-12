"""Classificação simples de intenção de consulta."""


class QueryClassificationService:
    """Classifica consultas em tipos para política de recuperação."""

    def classify(self, question: str, hint: str | None = None) -> str:
        if hint:
            return hint
        lowered = question.lower()
        if "norma" in lowered or "política" in lowered:
            return "normative_lookup"
        if "como" in lowered or "passo" in lowered:
            return "procedural"
        return "general"
