#!/usr/bin/env python3

from yt_dlp import YoutubeDL
import feedparser
import sqlite3

YT_BASE_FEEDURL = "https://www.youtube.com/feeds/videos.xml?channel_id="

# Take in base url of channel, on each run, get the chat URL:
# e.g. 
# input: 
# output: https://www.youtube.com/live_chat?is_popout=1&v=JmG_lrensuM

# Kamioshi Prototype
# Milestone 1
# - Parse Youtube channel content as Feed
# - Download videos in best quality/codec (vp9 or higher)
# - Find a way to sensibliy sort the files into subdirectories
# Milestone 2
# - Download in mobile quality

def get_livestream_chaturl(username):
    # Get channel ID from provided name/URL
    i = 0
    with YoutubeDL({'playlist_items':str(i)}) as ydl:
        info = ydl.extract_info("https://www.youtube.com/@%s/streams" % username, download=False)
        stream = info['entries'][0]
        if
        streamid = stream['id']
        chaturl = "https://www.youtube.com/live_chat?is_popout=1&v=%s" % streamid
        return chaturl


def main():
    # TODO: start with URL
    username = "zekutokairin"
    chaturl = get_livestream_chaturl(username)
    print(chaturl)


    # https://www.youtube.com/feeds/videos.xml?channel_id=UC2TveK-Kfbp8Wh3PeBh2i6A
    #addYoutubeChannel("https://www.youtube.com/@zekutokairin")

if __name__ == "__main__":
    main()
