#!/usr/bin/env python3

import os
import sys
from yt_dlp import YoutubeDL

def rename(video):
    """
    In case the download filename has been botched, this can fix the format
    """
    # Of all things, it's the '/' character being different that's throwing us off here.
    # We may just be able to strip out the Username title part and just go by title alone maybe
    local_path = "/mnt/e/Hizaki_Gamma"

    sys.exit(1)

def parse_channel():
    with YoutubeDL(params={"ignoreerrors":True}) as ydl:
        
        #3playlist_info = ydl.extract_info("https://www.youtube.com/watch?v=vWLz0vajpz4&list=PLDHlO0MJdqvXpYyf_DKaNgOYaKklXLJVv", download=False)
        for video in playlist_info['entries']:
            k
        #playlist_info = ydl.extract_info("https://www.youtube.com/@totalsizetest7968", download=False)
        #download_playlists(playlist_info)

        #channel_info = ydl.extract_info("https://www.youtube.com/@HizakiGamma/playlists", download=False)
        """
        This returns an info object
        info['entries'] appears to have 3 components, I think:
        0 Videos
        1 Live
        2 Shorts
        """
        import code
        code.interact(local=locals())

if __name__ == "__main__":
    parse_channel()

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
