#!/usr/bin/env python3

from yt_dlp import YoutubeDL

#with YoutubeDL({'playlist_items':'1'}) as ydl:
with YoutubeDL(params={"ignoreerrors":True}) as ydl:
    """
    This returns an info object
    info['entries'] appears to have 3 components, I think:
    0 Videos
    1 Live
    2 Shorts
    """
    # TODO: Download movies in Playlists, add entry to DB
    # TODO: Download movies in Live, add entry to DB
    # TODO: Download movies in Shorts, add entry to DB
    # TODO: Go through all movies in channel, download IFF not in DB
    #info = ydl.extract_info("https://www.youtube.com/@HizakiGamma", download=False)
    info = ydl.extract_info("https://www.youtube.com/@HizakiGamma/playlists", download=False)

    import code
    code.interact(local=locals())

# Code to get URLs of videos from playlist
"""

URL_PLAYLIST = "https://www.youtube.com/playlist?list=YOUR-LINK"

# Retrieve URLs of videos from playlist
playlist = Playlist(URL_PLAYLIST)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    urls.append(url)

print(urls)
"""
