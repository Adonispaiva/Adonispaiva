from app.domain.services.authority_resolution import AuthorityResolutionService


def test_documento_mestre_vence_snapshot() -> None:
    service = AuthorityResolutionService()
    assert service.compare("canonical", "snapshot") > 0


def test_canonical_vence_historical() -> None:
    service = AuthorityResolutionService()
    assert service.compare("canonical", "historical") > 0


def test_sovereign_vence_operational() -> None:
    service = AuthorityResolutionService()
    assert service.compare("sovereign", "operational") > 0


def test_normative_vence_canonical() -> None:
    service = AuthorityResolutionService()
    assert service.compare("normative", "canonical") > 0


def test_operational_vence_historical() -> None:
    service = AuthorityResolutionService()
    assert service.compare("operational", "historical") > 0
