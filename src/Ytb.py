import eel
from pytube import YouTube
import os

eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/web')


@eel.expose
def ytDownload(link: str, path_to_save: str = "./", resolution: str = "720p"):
    try:
        target = YouTube(link)
        target.streams.filter(file_extension="mp4").get_by_resolution(
            resolution).download(path_to_save)
    except:
        return False
    return True


@eel.expose
def openFolder():
    os.startfile(os.getcwd())


eel.start('index.html', size=(720, 600))
