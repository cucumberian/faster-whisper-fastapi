import os
from typing import Literal

import uvicorn
from fastapi import FastAPI, Response, UploadFile, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse, RedirectResponse

from depends import model, lock
from router.v2.v2_router import v2_router
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
app.include_router(v2_router)


@app.get("/", include_in_schema=False)
def docs():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transcribe", deprecated=True)
async def transcribe(
    response: Response, audio: UploadFile
) -> dict[Literal["response", "status"], str]:
    async with lock:
        try:
            segments, info = model.transcribe(audio=audio.file, beam_size=5)
            text = "".join([segment.text for segment in segments])
            return {
                "status": "ok",
                "response": text,
            }
        except Exception as e:
            response.status_code = 500
            return {
                "status": "error",
                "response": f"error: {e}",
            }


@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": str(exc)}
    )


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=True,
    )
