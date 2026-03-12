"""Router placeholder de memory."""

from fastapi import APIRouter

router = APIRouter(prefix="/memory", tags=["memory"])

@router.get("/")
def root() -> dict[str,str]:
    return {"status": "not_implemented", "module": "memory"}
