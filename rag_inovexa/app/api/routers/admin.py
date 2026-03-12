"""Router placeholder de admin."""

from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/")
def root() -> dict[str,str]:
    return {"status": "not_implemented", "module": "admin"}
