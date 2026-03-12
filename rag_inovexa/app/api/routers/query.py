"""Router de consultas RAG."""

from fastapi import APIRouter, Depends

from app.api.deps import get_run_query_use_case
from app.application.use_cases.run_query import RunQueryUseCase
from app.schemas.query import RetrieveQueryRequest, RetrieveQueryResponse

router = APIRouter(prefix="/query", tags=["query"])


@router.post("/retrieve", response_model=RetrieveQueryResponse)
def retrieve(
    payload: RetrieveQueryRequest,
    use_case: RunQueryUseCase = Depends(get_run_query_use_case),
) -> RetrieveQueryResponse:
    return use_case.execute(payload)
