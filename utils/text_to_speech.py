from elevenlabs import ElevenLabs
import os

# Ensure API key is set
api_key = os.getenv("ELEVEN_LABS_API")
if not api_key:
    raise ValueError("API key is missing. Set ELEVEN_LABS_API as an environment variable.")

# Initialize ElevenLabs client
client = ElevenLabs(api_key=api_key)

def text_to_speech(text, output_path="output.mp3"):
    if not text:
        raise ValueError("Text is empty. Cannot generate speech.")

    # Get audio as a generator (streamed chunks)
    audio_generator = client.text_to_speech.convert(text=text, voice_id="9BWtsMINqrJLrRacOk9x")

    # Save generator chunks to file
    with open(output_path, "wb") as f:
        for chunk in audio_generator:
            f.write(chunk)

    print(f"TTS audio saved: {output_path}")
    return output_path


