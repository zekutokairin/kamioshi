#!/usr/bin/env python3
import feedparser

from yt_dlp import YoutubeDL
#import yt_dlp as yt
#YoutubeDL = yt.YoutubeDL()

YT_BASE_FEEDURL = "https://www.youtube.com/feeds/videos.xml?channel_id="

# Kamioshi Prototype
# Milestone 1
# - Parse Youtube channel content as Feed
# - Download videos in best quality/codec (vp9 or higher)
# - Find a way to sensibliy sort the files into subdirectories
# Milestone 2
# - Download in mobile quality

def initializeDB():
    # TODO
    pass

def get_channel_id(username):
    # Get channel ID from provided name/URL
    with YoutubeDL({'playlist_items':'1'}) as ydl:
        info = ydl.extract_info("https://www.youtube.com/@zekutokairin", download=False)
    title = info['title']
    channel_id = info['channel_id']
    return channel_id

def addYoutubeChannel(url):
    # TODO: Parse results and create entries in the DB
    pass

# TODO: This is for published videos-- can we possibly get Lives as well?
def parseChannelRSS(channel_id):
    d = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)
    for entry in d.entries:
        print("ID: %s\tTitle: %s\tURL:%s" % (entry.id, entry.title, entry.link))

def main():
    username = "zekutokairin"
    channel_id = get_channel_id(username)

    parseChannelRSS(channel_id)
    
    # https://www.youtube.com/feeds/videos.xml?channel_id=UC2TveK-Kfbp8Wh3PeBh2i6A
    #addYoutubeChannel("https://www.youtube.com/@zekutokairin")

if __name__ == "__main__":
    main()
