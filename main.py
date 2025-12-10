from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
from TTS.api import TTS

app = FastAPI()

# Model sadece ilk başlatmada indirilir ve RAM'e alınır
tts = TTS("tts_models/tr/common-finetuned_ljspeech").to("cpu")

@app.get("/")
def home():
    return {"status": "Coqui TTS API Active 🎙️"}

@app.get("/tts")
def generate(text: str):
    file_name = f"audio_{uuid.uuid4()}.wav"
    output_path = Path(file_name)

    tts.tts_to_file(text=text, file_path=output_path)

    return FileResponse(output_path, media_type="audio/wav", filename=file_name)
