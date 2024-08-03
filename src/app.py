import os
from typing import Literal

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import Response
import uvicorn

from faster_whisper import WhisperModel


models_dir = os.path.join(os.path.dirname(__file__), "whisper_models/")
if not os.path.exists(models_dir):
    os.mkdir(models_dir)

model_size = os.getenv("MODEL_SIZE", "tiny")
model = WhisperModel(
    model_size_or_path=model_size,
    device="auto",
    compute_type="int8",
    download_root=models_dir,
    local_files_only=False,
)


app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/transcribe")
async def transcribe(
    response: Response, audio: UploadFile
) -> dict[Literal["response", "status"], str]:
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


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
