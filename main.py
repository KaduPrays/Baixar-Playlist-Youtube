import os
import pathlib
try:
    from pytube import YouTube
    from pytube import Playlist
    from pytube.exceptions import RegexMatchError
except ModuleNotFoundError:
    os.system('pip install pytube')

print('Developed by Fabbin ^^')

# Exemplo de links abaixo: #
# https://music.youtube.com/playlist?list=PLWaUTGTsLgBqShpW8TyRpl_j8noyiz5s_ #
# https://www.youtube.com/playlist?list=PLWaUTGTsLgBqShpW8TyRpl_j8noyiz5s_ #
# https://www.youtube.com/watch?v=2OyEECfNC8c&list=PLWaUTGTsLgBqShpW8TyRpl_j8noyiz5s_ #

PlaylistId = Playlist(input('Link da playlist: '))

for lista in PlaylistId:
     try:
         ys = YouTube(lista)
         print(f'[Youtube] - Musica encontrada: {ys.title}')
     except RegexMatchError:
         print(f'[Youtube] - Musica não encontrada: {ys.title}')
     else:
        checkmp3 = pathlib.Path(f'./music/{ys.title}.mp3')
        checkmp4 = pathlib.Path(f'./music/{ys.title}.mp4')
        if checkmp3.exists ():
            print (f'[Log] - Musica {ys.title} já salva.')
        else:
            if checkmp4.exists ():
                print(f'[Log] - Musica {ys.title} já salva.')
            else:
                    v = ys.streams.get_audio_only()
                    out_file = v.download(output_path="music")
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    print(f'[Log] - Musica salva: {ys.title}')