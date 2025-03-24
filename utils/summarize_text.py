import requests
import os
from dotenv import load_dotenv
import json
# Load environment variables
load_dotenv()

# Retrieve the API key from the environment
api_key = os.getenv('API_KEY')

def summarize_text(text: str) -> str:

   
    
    api_base_url=f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}'
    headers = {"Content-Type": "application/json"}
  
    prompt=f"""
You are an expert YouTube assistant.

You are given a full **transcription of a video**. Your job is to:
1. Classify the video type: e.g. educational, how-to/tutorial, entertainment, podcast, challenge, vlog, etc.
2. Summarize it clearly and helpfully based on that classification.

---

📚If the video is educational or tutorial-based**:
- Start with a short **overview** of what the video teaches or explains.
- Then, break down the video into **sections with clear headings**.
- Under each heading, give a **detailed summary** of that part of the video.
- Use bullet points or lists where useful.
- Keep the tone informative and clear.

If the video is entertainment, vlog, or challenge-based**:
- Summarize the general flow of what happens in the video.
- Highlight any unique moments, humor, or challenges.
- Keep the tone casual and fun, but still structured.

*If the transcript is too short or lacks content**, return it as-is without modification.

---

Video Transcript**:
This video is about:
{text}

---

Now classify and summarize the video accordingly.
"""


    payload = {
        "contents":[
            {
                "parts":[
                    {
                        "text":prompt
                    }
                ]
            }
        ]
    }
    try:
        response=requests.post(api_base_url,headers=headers,data=json.dumps(payload))
        response.raise_for_status() 
        summary=response.json()['candidates'][0]['content']['parts'][0]['text']
        summary=summary.replace("**","")
        return summary
    except Exception as e:
        print(f"Failed to summarize text: {e}")
        return None
        