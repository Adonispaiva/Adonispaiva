"""Regras de supersessão documental."""

from app.domain.services.authority_resolution import AuthorityResolutionService


class SupersessionService:
    """Aplica regras de substituição entre versões/documentos."""

    def __init__(self) -> None:
        self.authority = AuthorityResolutionService()

    def can_supersede(self, new_status: str, old_status: str) -> bool:
        return self.authority.compare(new_status, old_status) >= 0
