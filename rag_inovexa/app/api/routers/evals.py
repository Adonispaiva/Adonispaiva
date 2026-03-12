"""Router placeholder de evals."""

from fastapi import APIRouter

router = APIRouter(prefix="/evals", tags=["evals"])

@router.get("/")
def root() -> dict[str,str]:
    return {"status": "not_implemented", "module": "evals"}
