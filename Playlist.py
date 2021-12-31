from pytube import YouTube
from pytube import Playlist

Link = input("insira o Link: ")#Receber o link do video

yt = Playlist(Link)

print(f"Titulo = {yt.title}")#escreve o titulo do video
print(f"Autor: {yt.author}")

for url in yt.video_urls:
    ys = YouTube(url)
    ythigh = ys.streams.get_highest_resolution()
    ythigh.download()
    print("Baixando...")

