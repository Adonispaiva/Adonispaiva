"""Resolução de autoridade documental e precedência."""

from dataclasses import dataclass


PRECEDENCE = {
    "sovereign": 100,
    "normative": 95,
    "canonical": 85,
    "operational": 70,
    "snapshot": 60,
    "derived": 50,
    "historical": 20,
}


@dataclass(slots=True)
class AuthorityContext:
    normative_status: str
    authority_override: int | None = None


class AuthorityResolutionService:
    """Define nível de autoridade e comparação de precedência."""

    def resolve_level(self, context: AuthorityContext) -> int:
        if context.authority_override is not None:
            return max(0, min(100, context.authority_override))
        return PRECEDENCE.get(context.normative_status, 0)

    def compare(self, left_status: str, right_status: str) -> int:
        """Retorna >0 se left vence, <0 se right vence, 0 se empate."""

        left = PRECEDENCE.get(left_status, 0)
        right = PRECEDENCE.get(right_status, 0)
        if left > right:
            return 1
        if right > left:
            return -1
        return 0
