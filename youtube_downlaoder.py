import youtube_dl
video = input('link:')
ydl_options = {}

with youtube_dl.YoutubeDL(ydl_options) as ydl:
    ydl.download([video])
