Youtube video summary generator 
once url is given , 
-> the audio is downloaded using yt_dlp

->audio is transcribed (to get video content) using whisper

-> summary generated based on transcript using gemini api 

->text converted to speech using eleven labs 

To run , 
1) create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2) pip install requirements.txt
3) run python app.py
4) the app runs in http://127.0.0.1:5000/

sample output:  https://youtu.be/v0MELJPhqkw

current scope:
1) only english voiced videos 
