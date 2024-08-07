#!/bin/bash

# Test Channel: Hizaki Gamma
URL="https://www.youtube.com/@HizakiGamma"
#URL="https://www.youtube.com/@ZekuTokairin"

# FIXME: There's definitely a more robust way to do this
DOMAIN=$(echo ${URL} | awk -F'/' '{print $1FS$2FS$3}')    
CHANNEL_NAME=$(echo ${URL} | awk -F'/@' '{print $2}')    
PLAYLIST_URL="$URL/playlists"
SHORTS_URL="$URL/shorts"
VIDEOS_URL="$URL/videos"
STREAMS_URL="$URL/streams"

# TODO: Split the url automatically to get the archive filename
echo "CHANNEL NAME IS: $CHANNEL_NAME"
echo "Playlist NAME IS: $PLAYLIST_URL"


# Download Shorts
echo "Downloading Shorts..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Shorts/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $SHORTS_URL

# Download Playlists
echo "Downloading Playlists..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $PLAYLIST_URL

# Download Videos
echo "Downloading Playlists..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Videos/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $VIDEOS_URL

# Download Livestreams
#echo "Downloading Livestreams..."
yt-dlp --verbose -f "bestvideo[vcodec!~='vp0?9'][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Livestreams/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $STREAMS_URL


