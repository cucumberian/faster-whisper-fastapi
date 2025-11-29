from fastapi import APIRouter, UploadFile

from depends import lock, model

transcribe_router = APIRouter(prefix="/transcribe", tags=["transcribe"])


@transcribe_router.post("")
async def transcribe(audio: UploadFile) -> str:
    async with lock:
        segments, _ = model.transcribe(audio=audio.file)
        text = "".join([segment.text for segment in segments])
        return text
