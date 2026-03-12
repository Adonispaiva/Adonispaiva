"""Router placeholder de governance."""

from fastapi import APIRouter

router = APIRouter(prefix="/governance", tags=["governance"])

@router.get("/")
def root() -> dict[str,str]:
    return {"status": "not_implemented", "module": "governance"}
