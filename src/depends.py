import os
from faster_whisper import WhisperModel
from dotenv import load_dotenv
import asyncio

lock = asyncio.Lock()

load_dotenv()


models_dir = os.path.join(os.path.dirname(__file__), "whisper_models/")
if not os.path.exists(models_dir):
    os.mkdir(models_dir)

model_size = os.getenv("MODEL_SIZE", "tiny")

model = WhisperModel(
    model_size_or_path=model_size,
    device="cpu",
    compute_type="int8",
    download_root=models_dir,
    local_files_only=False,
)
