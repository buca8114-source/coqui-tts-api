from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import subprocess
import uuid
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Coqui TTS API Active 🎙️"}

@app.get("/tts")
def tts(text: str):
    file_name = f"audio_{uuid.uuid4()}.wav"
    output_path = Path(file_name)

    command = f'tts --text "{text}" --out_path "{output_path}"'
    subprocess.call(command, shell=True)

    return FileResponse(output_path, media_type="audio/wav", filename=file_name)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
