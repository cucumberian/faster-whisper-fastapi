from fastapi import APIRouter
from router.v2.transcribe_router import transcribe_router

v2_router = APIRouter(prefix="/v2")


v2_router.include_router(transcribe_router)
