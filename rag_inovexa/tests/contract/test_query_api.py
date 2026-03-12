from fastapi.testclient import TestClient

from app.main import app


def test_retrieve_query_contract() -> None:
    client = TestClient(app)
    response = client.post(
        "/v1/query/retrieve",
        json={
            "question": "Qual a política de arquitetura vigente?",
            "project": "gpt-inovexa",
            "need_memory": True,
            "max_candidates": 5,
            "max_context_chunks": 3,
            "allow_historical": False,
            "sensitivity_mode": "internal",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert "query_id" in payload
    assert "selected_collections" in payload
    assert "recommended_context_bundle_id" in payload
