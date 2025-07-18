# REST API 엔드포인트 예시
from fastapi import APIRouter

router = APIRouter()

@router.get('/status')
def get_status():
    return {"status": "ok"}
