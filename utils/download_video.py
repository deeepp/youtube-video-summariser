import yt_dlp
import os
 # Add this line

def download_video(url: str, download_path: str = 'downloads/'):
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Corrected Key
            'preferredcodec': 'mp3',
            'preferredquality': '192',
          
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict.get('title', None)
        print(f"Downloaded: {title}")

    audio_file_path = os.path.join(download_path, f"{info_dict['id']}.mp3")
    
    if os.path.exists(audio_file_path):
        print(f"Downloaded audio file path: {audio_file_path}")
    else:
        print(f"Audio file not found: {audio_file_path}")
    
    return audio_file_path
