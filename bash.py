import yt_dlp

def baixar_mp3(url, pasta_destino=""):
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookiefile': 'www.youtube.com_cookies.txt',
        'remote_components': ['ejs:github'],
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=SHhZTEL-0sA"
    baixar_mp3(video_url)