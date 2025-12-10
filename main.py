from fastapi import FastAPI
from fastapi.responses import FileResponse
import uuid
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Coqui TTS API Active 🚀"}

@app.post("/tts")
def tts(text: str, voice: str="tts_models/en/ljspeech/tacotron2-DDC"):
    filename = f"{uuid.uuid4()}.wav"
    cmd = f'tts --text "{text}" --model_name "{voice}" --out_path {filename}'
    subprocess.run(cmd, shell=True)
    return FileResponse(filename, media_type="audio/wav", filename=filename)
