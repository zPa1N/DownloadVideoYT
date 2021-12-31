from pytube import YouTube
from pytube.cli import on_progress

Link = input("Link do video: ")#Receber o link do video
yt = YouTube(Link)#procura o Link no Youtube

print(f"Titulo = {yt.title}")#escreve o titulo do video
print(f"Autor do video: {yt.author}")#escreve o autor do video
print("Baixando...")

ythigh = yt.streams.get_highest_resolution()#verifica a maior resoluçaõ disponivel no video 
ythigh.download()#começa o download do video