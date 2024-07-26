#!/usr/bin/env python3

from yt_dlp import YoutubeDL

def enqueue_videos(info, prefix):
    # In the case of playlists, the prefix is the Playlist Title
    # Otherwise, prefix is either Videos, Shorts, or Live
    # TODO
    pass

def download_playlists(playlist_info):
    

def parse_channel(url):
    with YoutubeDL(params={"ignoreerrors":True}) as ydl:
        # TODO: Download movies in Playlists, add entries to DB
        playlist_info = ydl.extract_info("https://www.youtube.com/@HizakiGamma/playlists", download=False)
        download_playlists(playlist_info)

        channel_info = ydl.extract_info("https://www.youtube.com/@HizakiGamma/playlists", download=False)

        """
        This returns an info object
        info['entries'] appears to have 3 components, I think:
        0 Videos
        1 Live
        2 Shorts
        """
        # TODO: Download movies in Live, add entry to DB 
        # TODO: Download movies in Shorts, add entry to DB
        # TODO: Go through all movies in channel
        #info = ydl.extract_info("https://www.youtube.com/@HizakiGamma", download=False)

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
