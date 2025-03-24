
import os
import whisper

import requests
from flask import Flask, request, render_template, jsonify,send_file
from gtts import gTTS
from dotenv import load_dotenv
from utils.download_video import download_video
from utils.transcribe_audio import transcribe_audio
from utils.summarize_text import summarize_text
from utils.text_to_speech import text_to_speech

load_dotenv()   
app= Flask(__name__)
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
whisper_model = whisper.load_model("base")
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        video_url = request.form.get("url")
        print(f"Received video URL: {video_url}")  # Debug log for URL

        if not video_url:
            return jsonify({"error": "No video URL provided"}), 400

        # Transcription and summarization
        audio_file_path = download_video(video_url)
        transcription = transcribe_audio(audio_file_path)
        summary = summarize_text(transcription)

        if not summary:
            return jsonify({"error": "Summarization failed"}), 500

        # Generate TTS audio from summary
        audio_path= text_to_speech(summary, output_path=os.path.join(UPLOAD_FOLDER, "output.mp3"))

        return jsonify({
            "received_url": video_url,
            "transcription": transcription,
            "summary": summary,
            "audio_url": "/static/output.mp3"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
   

@app.route("/tts", methods=["POST"])
def tts():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        output_path = os.path.join(UPLOAD_FOLDER, "output.mp3")
        tts = gTTS(text=text, lang="en")
        tts.save(output_path)

        return send_file(output_path, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    sample_text = """
    Whisper is an automatic speech recognition system trained on 680,000 hours of multilingual and multitask supervised data collected from the web.
    It shows strong performance on a variety of benchmarks and tasks and is open-sourced by OpenAI.
    """
    print(summarize_text(sample_text))
    app.run(debug=True)
