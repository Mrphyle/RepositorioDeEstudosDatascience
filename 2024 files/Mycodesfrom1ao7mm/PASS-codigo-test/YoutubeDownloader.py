from pytube import YouTube
def youtubedowloader():
    url = input("Coloque a URL do vídeo: ")
    video = YouTube(url)
    print('Baixando video....')
    download = video.streams.get_highest_resolution()
    downloadpath = r"C:\Users\hoolf\Videos"
    download.download(downloadpath)
    print('O download foi um sucesso!')
while True:
    youtubedowloader()
    ResetTube = input("Deseja baixar outro video? ")
    print("___________________________________")
    if ResetTube.lower() not in ['yes', 'sim', '1']:
        print('Encerrado')
        break