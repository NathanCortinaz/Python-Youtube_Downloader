from __future__ import unicode_literals
import eel
import youtube_dl
import os

eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/web')
# eel.init('web')


@eel.expose
def ytDownload(link):
    options = {}
    with youtube_dl.YoutubeDL(options) as ytDownloadLink:
        ytDownloadLink.download(link)


eel.start('index.html', size=(1000, 600))
