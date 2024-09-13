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

def get_channel_id(username):
    # Get channel ID from provided name/URL
    with YoutubeDL({'playlist_items':'1'}) as ydl:
        info = ydl.extract_info("https://www.youtube.com/@%s" % username, download=False)
        import code

        code.interact(local=locals())
    title = info['title']
    channel_id = info['channel_id']
    return channel_id

def addYoutubeChannel(url):
    # TODO: Parse results and create entries in the DB
    pass

# TODO: Is doing this even a good idea? TBH there's already a good job being done by yt-dlp retrieving all video info
def parseChannelRSS(channel_id):
    d = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)
    for entry in d.entries:
        print("ID: %s\tTitle: %s\tURL:%s" % (entry.id, entry.title, entry.link))

    import code

def main():
    # TODO: start with URL
    username = "zekutokairin"
    channel_id = get_channel_id(username)

    parseChannelRSS(channel_id)
    # https://www.youtube.com/feeds/videos.xml?channel_id=UC2TveK-Kfbp8Wh3PeBh2i6A
    #addYoutubeChannel("https://www.youtube.com/@zekutokairin")

if __name__ == "__main__":
    main()
