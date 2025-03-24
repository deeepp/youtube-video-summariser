import whisper
model = whisper.load_model("base")
def transcribe_audio(audio_path: str):
    if not audio_path:
        raise ValueError("Audio file path is None or invalid.")
    print(f"Transcribing audio file: {audio_path}")
    result = model.transcribe(audio_path)  # Assuming you're using Whisper
    # print(f"Transcription result: {result}")
    if 'text' in result:
        return result['text']
    else:
        raise ValueError("Failed to transcribe audio.")
