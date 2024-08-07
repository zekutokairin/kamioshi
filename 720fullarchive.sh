#!/bin/bash

# Test Channel: Hizaki Gamma
#URL="https://www.youtube.com/@HizakiGamma"
URL="https://www.youtube.com/@ZekuTokairin"

# FIXME: There's definitely a more robust way to do this
DOMAIN=$(echo ${URL} | awk -F'/' '{print $1FS$2FS$3}')    
CHANNEL_NAME=$(echo ${URL} | awk -F'/@' '{print $2}')    
PLAYLIST_URL="$URL/playlists"

# TODO: Split the url automatically to get the archive filename
echo "CHANNEL NAME IS: $CHANNEL_NAME"
echo "Playlist NAME IS: $PLAYLIST_URL"

# Download Playlists
echo "Downloading playlists..."
# Give it the URL to the playlists of the channel you want to archive
#yt-dlp --verbose -f "bestvideo[vcodec!~=vp0?9][height<=?720]+bestaudio/best[height<=?720]" --yes-playlist --write-auto-subs --embed-subs --embed-chapters --embed-thumbnail -o "%(channel)s/Playlists/%(playlist_title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --embed-chapters --download-archive $CHANNEL_NAME.txt $PLAYLIST_URL

# Download Shorts

# Download Videos

# Download Livestreams
